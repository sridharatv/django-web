from django.conf.urls import url
from myapp1 import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^image', views.image, name="image"),
    url(r'^video', views.awsrds, name="video"),
]