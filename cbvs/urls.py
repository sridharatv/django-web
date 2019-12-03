from django.conf.urls import url

from . import views

app_name = 'cbvs'

urlpatterns = [
    url(r'^$', views.LibraryListView.as_view(), name='index'),
    url(r'^list/$', views.LibraryListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.LibraryDetailView.as_view(), name='detail'),
]
