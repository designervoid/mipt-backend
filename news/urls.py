from django.urls import path
from .views import news_main


urlpatterns = [
    path('news_main/', news_main, name='news_main')
]
