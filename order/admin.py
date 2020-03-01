from django.contrib import admin

# Register your models here.

from .models import Claim, Feedback


admin.site.register(Claim)
admin.site.register(Feedback)

