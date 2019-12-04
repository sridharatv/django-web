from django.conf.urls import url

from . import views, book_views

app_name = 'cbvs'

urlpatterns = [
    url(r'^$', views.CBVSTemplateView.as_view(), name='index'),
    url(r'^list/$', views.LibraryListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.LibraryDetailView.as_view(), name='detail'),
    url(r'^create/$', views.LibraryCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.LibraryUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.LibraryDeleteView.as_view(), name='delete'),
    url(r'^book_list/$', book_views.BookListView.as_view(), name='book_list'),
    url(r'^book_list/(?P<pk>\d+)/$', book_views.BookDetailView.as_view(), name='book_detail'),
    url(r'^book_create/$', book_views.BookCreateView.as_view(), name='book_create'),
    url(r'^book_update/(?P<pk>\d+)/$', book_views.BookUpdateView.as_view(), name='book_update'),
    url(r'^book_delete/(?P<pk>\d+)/$', book_views.BookDeleteView.as_view(), name='book_delete'),
]

