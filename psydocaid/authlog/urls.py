from django.contrib import admin
from django.urls import path, include
from authlog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signupUser, name="signup"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('tweets', include('tweets.urls'))
]
