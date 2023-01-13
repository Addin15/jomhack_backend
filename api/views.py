from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from users.models import CustomUser
from knox.auth import AuthToken
from django.contrib.auth import authenticate

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

    print(data['email'])
    print(data['password'])

    user = CustomUser.objects.filter(email=data['email']).filter(password=data['password']).first()
    if not user:
        return Response(data={'message':'user not found'}, status=status.HTTP_404_NOT_FOUND)        

    token = AuthToken.objects.create(user=user)[1]

    user = UserSerializer(user)

    return Response(data={'user': user.data, 'token': token}, status=status.HTTP_200_OK)
    