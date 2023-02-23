from django.contrib import admin
from django.urls import path
from manage_carservice import views

urlpatterns = [
    path('newservice/', views.newservice),
    path('login/', views.login)
]