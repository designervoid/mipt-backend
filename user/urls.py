from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registry/', views.registry, name='registry'),
    path('detail/<str:first_name>/', views.detail, name='detail'),
]