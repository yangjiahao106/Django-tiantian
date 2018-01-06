from django.db import models

# Create your models here.
class Cart(models.Model):
    uid = models.ForeignKey('app_user.UserInfo')
    gid = models.ForeignKey('app_goods.GoodsInfo')
    gnumber = models.IntegerField(default=1)
    isselect = models.BooleanField(default=True)


class OrderInfo(models.Model):
    onumber = models.CharField(max_length=20)
    uid = models.ForeignKey('app_user.UserInfo')
    ototal = models.DecimalField(max_digits=6, decimal_places=2)
    odate = models.DateField(auto_now=True)
    oispay = models.BooleanField(default=False)
    oaddress = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    oid = models.ForeignKey('OrderInfo')
    gid = models.ForeignKey('app_goods.GoodsInfo')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField()
