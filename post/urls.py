from . import views
from django.urls import path , include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts' , views.PostView)
router.register(r'category' , views.CategoryView)
router.register(r'comment' , views.CommentsView)

urlpatterns = [
    path('', include(router.urls) , name='register'),
]