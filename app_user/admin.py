from django.contrib import admin

# Register your models here.

from .models import UserInfo, BrowseHistory, UserAddress

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','uname']


class BrowseHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'gid']
    list_per_page = 15

class UserAddreddAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'address']
    list_per_page = 15

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(BrowseHistory, BrowseHistoryAdmin)
admin.site.register(UserAddress, UserAddreddAdmin)