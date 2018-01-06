from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'', views.index),
    url(r'^index$', views.index),
    url(r'^detail(\d+)$', views.detail),
    url(r'^list(\d+)', views.list)
    # url(r'^', views.detail)
]