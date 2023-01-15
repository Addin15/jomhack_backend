from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import AssestmentSerializer, EditSerializer, NewsSerializer, UploadPhotoSerializer, UserSerializer, LoginSerializer, PlanSerializer
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

    id = user.id

    user = UserSerializer(user)

    user_data = user.data

    user_data['assestment'] = None

    assestment = models.Assestment.objects.filter(user_id=id).first()

    if assestment is not None:
        assestment_serializer = AssestmentSerializer(assestment)

        user_data['assestment'] = assestment_serializer.data

    return Response(data={'user': user_data, 'token': token}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user(request):
    user = request.user
    serializer = UserSerializer(user)
    data = serializer.data
    data['assestment'] = None

    assestment = models.Assestment.objects.filter(user_id=user.id).first()

    if assestment is not None:
        assestment_serializer = AssestmentSerializer(assestment)

        data['assestment'] = assestment_serializer.data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit(request):
    user = request.user
    serializer = EditSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data

    if (request.FILES.get('image') is not None):
        data['image'] = request.FILES.get('image')

    user.name = data['name']
    user.image = data['image']
    user.save()

    return Response(data={'message': 'success'}, status=status.HTTP_200_OK)


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

    assestment = models.Assestment.objects.filter(user_id=user.id).first()

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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def news(request):
    user = request.user

    # TODO: use AI to get keys for the plan
    keys = ['Life', 'Disease', 'Medical']

    news = models.News.objects.all()

    related_news = []

    for n in news:
        matched = 0
        for key in keys:
            if key in n.keys:
                matched += 1

        if matched > 0:
            related_news.append(n)

    serializer = NewsSerializer(related_news, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upload_photo(request):
    user = request.user
    file = request.FILES

    serializer = UploadPhotoSerializer(data=file)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data

    user.image = data['image']
    user.save()

    return Response(data={'message': 'success'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def assestment(request):
    user = request.user
    data = request.data

    serializer = AssestmentSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    data['user_id'] = user.id

    assestment = models.Assestment.objects.create(**data)

    serializer = AssestmentSerializer(assestment)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
