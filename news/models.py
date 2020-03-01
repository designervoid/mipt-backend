from django.db import models

# Create your models here.


class News(models.Model):
    header = models.CharField(max_length=20)
    short_descriptions = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    mark_text = models.CharField(max_length=40)
    mark_color = models.CharField(max_length=7)
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header