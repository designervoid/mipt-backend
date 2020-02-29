from django.shortcuts import render

# Create your views here.


def login(request):
    context = {}
    return render(request, 'login.html', context)


def registry(request):
    context = {}
    return render(request, 'registry.html', context)


def logout(request):
    context = {}
    return render(request, 'logout.html', context)


def detail(request, first_name):
    context = {}
    return render(request, 'detail.html', context)