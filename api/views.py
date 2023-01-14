from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer, PlanSerializer
from users.models import CustomUser
from knox.auth import AuthToken, TokenAuthentication
from django.contrib.auth import authenticate
from . import models

# Create your views here.


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    user = CustomUser.objects.create(**data)

    token = AuthToken.objects.create(user)[1]

    user = UserSerializer(user)

    return Response(data={'user': user.data, 'token': token}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    user = CustomUser.objects.filter(email=data['email']).filter(
        password=data['password']).first()
    if not user:
        return Response(data={'message': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    # user = authenticate(email=data['email'], password=data['password'])

    token = AuthToken.objects.create(user=user)[1]

    user = UserSerializer(user)

    return Response(data={'user': user.data, 'token': token}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def plans(request):
    plans = models.Plans.objects.all()
    serializer = PlanSerializer(plans, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_plans(request):
    user = request.user

    # TODO: use AI to get keys for the plan
    keys = ['Life', 'Disease', 'Medical']

    plans = models.Plans.objects.all()

    related_plans = []

    for plan in plans:
        matched = 0
        for key in keys:
            if key in plan.keys:
                matched += 1

        if matched > 0:
            related_plans.append(plan)

    serializer = PlanSerializer(related_plans, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
