from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def login(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def registry(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def logout(request):
    return HttpResponse("Hello, world. You're at the polls index.")