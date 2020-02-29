from django.shortcuts import render

# Create your views here.
def old(request):
    context = {}
    return render(request, 'old.html', context)

def new(request):
    context = {}
    return render(request, 'new.html', context)