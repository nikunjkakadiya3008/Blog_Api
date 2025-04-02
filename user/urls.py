from . import views
from django.urls import path

app_name = 'User'
urlpatterns = [
    path('register/', views.RegisterUser.as_view() , name='register'),
    path('login',views.LoginView.as_view() , name='Login'),
    path('logout',views.LogoutView.as_view() , name='Logout'),
    path('refresh',views.RefreshView.as_view() , name='refresh'),
]
