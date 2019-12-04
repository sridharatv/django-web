from django.conf.urls import url

from . import views

app_name = 'cbvs'

urlpatterns = [
    url(r'^$', views.LibraryListView.as_view(), name='index'),
    url(r'^list/$', views.LibraryListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.LibraryDetailView.as_view(), name='detail'),
    url(r'^create/$', views.LibraryCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.LibraryUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.LibraryDeleteView.as_view(), name='delete'),

]

