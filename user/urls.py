from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('find-friends/', views.findfriends, name='findfriends'),
    path('my-profile/', views.myprofile, name='myprofile'),
    path('send-req/<int:pk>/', views.sendreq, name='send-req'),
    path('accept-req/<int:pk>/', views.acceptreq, name='accept-req'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]