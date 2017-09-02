
from django.conf.urls import include, url
from . import views
urlpatterns = [

    url(r'^$', views.index2,  name='index'),
]
