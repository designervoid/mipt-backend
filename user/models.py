from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    room = models.FloatField()
    group = models.CharField(max_length=5)
    passwd = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Orders(models.Model):
    id_order = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.TextField()
    theme = models.CharField(max_length=40)
    tags = models.CharField(max_length=20)
    created_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body