from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="form_index"),
    url(r'^signup', views.signup, name="signup"),
]
