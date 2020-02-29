from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class User(models.Model):
    # id = models.ForeignKey(on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    room = models.IntegerField()
    group = models.CharField(max_length=5)
    passwd = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
