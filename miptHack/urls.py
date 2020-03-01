"""miptHack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index
from user.models import User, Orders
from order.models import Claim, Feedback
from news.models import News
from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from django.views.generic import TemplateView



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'room', 'group']


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ['body', 'role_user', 'created_data', 'comments', 'progress_user']


class ClaimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Claim
        fields = ['id_order', 'executor', 'role', 'info', 'progress']


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['header', 'short_descriptions', 'text', 'mark_text', 'mark_color', 'date_published']


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ['question', 'date', 'answer', 'check_ans']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('-created_data')
    message = queryset[0]
    serializer_class = OrdersSerializer


class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all().order_by('-progress')
    serializer_class = ClaimSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-date_published')
    serializer_class = NewsSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('-date')
    serializer_class = FeedbackSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'claims', ClaimViewSet)
router.register(r'news', NewsViewSet)
router.register(r'feedback', FeedbackViewSet)




urlpatterns = [
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),

    path('', TemplateView.as_view(template_name='application.html'),
    name='app'),
]
