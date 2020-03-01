from django.shortcuts import render

# Create your views here.
def news_main(request):
    context={}
    return render(request, 'news.html', context)