from django.conf.urls import url
from relurl import views

app_name = "relurl"

urlpatterns = [
    url (r'^$', views.index, name='index'),
    url(r'^image/$', views.image, name='image'),
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^templ/$', views.templ, name='templ'),
    url(r'^devices/$', views.devices, name='devices'),
]