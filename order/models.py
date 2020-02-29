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

    id_order = models.OneToOneField(Orders, on_delete=models.DO_NOTHING)
    executor = models.CharField(max_length=20)
    role = models.CharField(max_length=2, choices=ROLES)
    cost = models.IntegerField()
    tools = models.CharField(max_length=40)
    info = models.CharField(max_length=200)


    def __str__(self):
        return self.executor
