from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mycart$', views.mycart),
    url(r'^order$', views.order),
    url(r'^add(\d+)_(\d+)', views.add_cart),
    url(r'^update_cart$', views.updata_cart),
    url(r'^update_select$', views.update_select),
    url(r'^order_handle$', views.order_handle)
]