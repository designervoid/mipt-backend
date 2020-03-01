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
    ROLES_USER = (
        ('pl', 'plumber'),
        ('cl', 'cleaner'),
        ('ex', 'exterminator'),
        ('el', 'electrician'),
        ('nu', 'nurse'),
        ('se', 'security'),
    )
    STATUS_USER = (
        ('cd', 'considuration'),
        ('pf', 'performed'),
        ('rj', 'rejected'),
        ('rd', 'ready'),
    )

    id_order = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.TextField()
    role_user = models.CharField(max_length=2, choices=ROLES_USER)
    created_data = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=30)
    progress_user = models.CharField(max_length=2, choices=STATUS_USER)

    def __str__(self):
        return self.body