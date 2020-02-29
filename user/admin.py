from django.contrib import admin

# Register your models here.

from .models import User, Orders

admin.site.register(User)
admin.site.register(Orders)