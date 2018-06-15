from django.urls import path, include
from django.contrib import admin
from .views import home, register

urlpatterns = [
    path('', home),
    path('register/', register),
]