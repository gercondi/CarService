from django.contrib import admin
from django.urls import path, re_path, include
from manage_carservice import views

urlpatterns = [

    #    indeca la pagina inicial del proyecto, cuando no se coloca ninguna pagina en la URL
    re_path(r'^$', views.index, name='index'),

    path('index/', views.index),
    path('newservice/', views.newservice),
    path('login/', views.login),
    path('accounts/', include('django.contrib.auth.urls')),
]