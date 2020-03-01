from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from .models import User, Orders

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
    if request.method == 'GET':
        info_orders = Orders.objects.all().order_by('-created_data')
        output = [q for q in info_orders]
    return JsonResponse(output, safe=False)