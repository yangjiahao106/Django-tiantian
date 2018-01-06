from django.db import models
from app_goods.models import GoodsInfo
# Create your models here.

class UserAddress(models.Model):
    recipient = models.CharField(max_length=20,default='')
    rphone = models.CharField(max_length=11, default='')
    address = models.CharField(max_length=100)
    rcode = models.CharField(max_length=6, default='')
    user = models.ForeignKey('UserInfo')

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=20)
    uphone = models.CharField(max_length=11, default='')
    ucode = models.CharField(max_length=6, default='')
    def __str__(self):
        return self.uname

class BrowseHistory(models.Model):
    uid = models.ForeignKey('UserInfo')
    gid = models.ForeignKey(GoodsInfo)

