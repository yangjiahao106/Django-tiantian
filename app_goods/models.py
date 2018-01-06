from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    tisdelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpicture = models.ImageField(upload_to='app_goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gunit = models.CharField(max_length=10)
    gclick = models.IntegerField()
    gtype = models.ForeignKey('TypeInfo')
    gisdelete = models.BooleanField(default=False)
    gsummary = models.CharField(max_length=200)
    gcontent = HTMLField()
    def __str__(self):
        return self.gtitle