from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import permissions , mixins
from rest_framework import generics
from . import serializers
from core import models
# from . import permissions


class PostView(viewsets.ModelViewSet):
    serializer_class =serializers.PostSerializer
    queryset = models.Post.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id = self.request.user.id)

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.request.method in permissions.SAFE_METHODS:
            return [permission() for permission in permission_classes]
        return [permission() for permission in self.permission_classes]


class CategoryView( mixins.ListModelMixin ,
                mixins.RetrieveModelMixin
               ,viewsets.GenericViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

