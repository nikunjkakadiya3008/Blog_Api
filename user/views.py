from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny , IsAuthenticated
from core import models
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from .serializers import UserSerializer , CredentialsSerializer , RefreshTokenSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CredentialsSerializer
    def _get_tokens_for_user(self , user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }
    def post(self , request ):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"detail":" username and password is requires"},status= status.HTTP_400_BAD_REQUEST )
        user = get_user_model().objects.get(username = username)


        if user is None:
            return Response(status= status.HTTP_401_UNAUTHORIZED)

        if(user.check_password(password)):
            token = self._get_tokens_for_user(user)
            return Response(token , status=status.HTTP_200_OK)
        return Response({"error":"Invalid Password"} , status= status.HTTP_400_BAD_REQUEST)


class RefreshView(APIView):
    serializer_class = RefreshTokenSerializer
    def _get_tokens_for_user(self , user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }

    def post (self , request):
        refresh_token = request.data.get('refresh_token')
        try:
            if refresh_token is None :
                return Response({"Error":"The refresh_token is not provided"})

            refresh = RefreshToken(refresh_token)
            if BlacklistedToken.objects.filter(token = refresh['user_id']).exists():
                return Response({"token_error":"Token is expired"} , status=status.HTTP_404_NOT_FOUND)

            refresh.blacklist()
            user = get_user_model().objects.get(pk = refresh['user_id'])
            token = self._get_tokens_for_user(user)
            return Response(token,
                             status=status.HTTP_200_OK
                            )
        except TokenError as e:
            return Response({"token Error":str(e)} , status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"token Error":str(e)}  , status= status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RefreshTokenSerializer

    def post(self, request):
        try:

            refresh_token = request.data.get('refresh_token')
            refresh = RefreshToken(refresh_token)
            access_token = request.headers.get('Authorization')
            if access_token and access_token.startswith('Bearer '):
                access_token =access_token.split(' ')[1]  # Return the token part
            else:
                access_token = refresh.access_token

            if not refresh_token:
                return Response({"detail": "Refresh token is missing."}, status=status.HTTP_400_BAD_REQUEST)


            models.BlacklistedAccessToken.objects.create(token=access_token)

            refresh.blacklist()

            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)