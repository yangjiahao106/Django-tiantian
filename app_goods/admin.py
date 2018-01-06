from django.contrib import admin

# Register your models here.

from .models import GoodsInfo
from .models import TypeInfo

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice']
    list_per_page = 15
    fields = [( 'gtitle', 'gprice')]



admin.site.register(GoodsInfo, GoodsInfoAdmin)
admin.site.register(TypeInfo, TypeInfoAdmin)