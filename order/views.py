from django.shortcuts import render

# Create your views here.
def old():
    return render(request, 'old.html', context)

def new():
    return render(request, 'new.html', context)