"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from myapp1 import views

urlpatterns = [
    #path('', views.index),
    url(r'^$', views.image, name="index"),
    url(r'booklist', views.index, name="index"),
    url(r'^myapp1/', include ('myapp1.urls')),
    url(r'^register/', include ('myform.urls')),
    url(r'^relurl/', include('relurl.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^cbvs/', include('cbvs.urls')),
    path('admin/', admin.site.urls),
]
