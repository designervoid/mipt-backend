from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
    path('registry/', views.registry, name='registry'),
    path('detail/<first_name>/', views.detail, name='detail'),
]