import django_filters.rest_framework
from rest_framework.filters import OrderingFilter
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import permissions , mixins
from rest_framework import generics ,status
from rest_framework.response import Response

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from datetime import datetime
from . import serializers
from core import models
from .filters import MyModelFilter
from .permissions import OnlyRead


class PostView(viewsets.ModelViewSet):
    serializer_class =serializers.PostSerializer
    queryset = models.Post.objects.all()
    permission_classes = [IsAuthenticated ,OnlyRead ]
    filter_backends = [filters.SearchFilter , django_filters.rest_framework.DjangoFilterBackend , filters.OrderingFilter  ]
    search_fields = ['title','content']
    # filterset_fields = ['Category','author']
    ordering_fields = ['author', 'created_at','Category']
    filterset_class = MyModelFilter
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(user_id = self.request.user.id)
        

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.request.method in permissions.SAFE_METHODS:
            return [permission() for permission in permission_classes]
        return [permission() for permission in self.permission_classes]

    # def get_queryset(self):
    #     queryset = models.Post.objects.all()
    #     category = self.request.query_params.get('category', None)

    #     if category is not None:
    #         print
    #         category_list = models.Category.objects.get(name = category)
    #         print(category_list)
    #         queryset = models.Post.objects.filter(Category = category_list.id)
    #         return queryset
    #     return self.queryset


class CategoryView( mixins.ListModelMixin ,
                mixins.RetrieveModelMixin
               ,viewsets.GenericViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class CommentsView(mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.request.method in permissions.SAFE_METHODS:
            return [permission() for permission in permission_classes]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(author_id = self.request.user.id)
