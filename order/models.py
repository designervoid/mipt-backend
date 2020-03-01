from django.db import models
from user.models import Orders

# Create your models here.
class Claim(models.Model):
    ROLES = (
        ('pl', 'plumber'),
        ('cl', 'cleaner'),
        ('ex', 'exterminator'),
        ('el', 'electrician'),
        ('nu', 'nurse'),
        ('se', 'security'),
    )
    STATUS = (
        ('cd', 'considuration'),
        ('pf', 'performed'),
        ('rj', 'rejected'),
        ('rd', 'ready'),
    )

    id_order = models.OneToOneField(Orders, on_delete=models.DO_NOTHING)
    executor = models.CharField(max_length=20)
    role = models.CharField(max_length=2, choices=ROLES)
    info = models.CharField(max_length=200)
    progress = models.CharField(max_length=2, choices=STATUS)

    def __str__(self):
        return self.executor


class Feedback(models.Model):
    question = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False)
    answer = models.CharField(max_length=100, default='')
    check_ans = models.BooleanField()

    def __str__(self):
        return self.question