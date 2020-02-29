from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('old/', views.old, name='old'),
    path('new/', views.new, name='new')
]