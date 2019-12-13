from django.urls import path
from .views import register,profile
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/up/', register, name='register'),
    path('profile/',profile, name = 'profile'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout')

]
