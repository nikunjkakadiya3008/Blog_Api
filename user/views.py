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
from rest_framework.throttling import UserRateThrottle



class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer


class ExampleView(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


# class LoginView(APIView):
#     permission_classes = [AllowAny]
#     serializer_class = CredentialsSerializer
#     queryset = get_user_model().objects.all()
#     def _get_tokens_for_user(self , user):
#         refresh = RefreshToken.for_user(user)
#         return {
#             "refresh":str(refresh),
#             "access":str(refresh.access_token)
#         }
#     def post(self , request ):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         if not username or not password:
#             return Response({"detail":" username and password is requires"},status= status.HTTP_400_BAD_REQUEST )
#         try:
#             user = get_user_model().objects.get(username = username)
#         except Exception:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


#         if user is None:
#             return Response(status= status.HTTP_401_UNAUTHORIZED)

#         if(user.check_password(password)):
#             token = self._get_tokens_for_user(user)
#             return Response(token , status=status.HTTP_200_OK)
#         return Response({"error":"Invalid Password"} , status= status.HTTP_400_BAD_REQUEST)





