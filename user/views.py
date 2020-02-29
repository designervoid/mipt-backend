from django.shortcuts import render
from django.http import HttpResponse

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
    info_orders = Orders.objects.order_by('-created_data')
    output = ', '.join([q.id_order for q in info_orders])
    return HttpResponse(output)