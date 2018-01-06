from django.contrib import admin
from .models import *

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'gid', 'gnumber']

admin.site.register(Cart, CartAdmin)
