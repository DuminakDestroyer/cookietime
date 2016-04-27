from django.conf.urls import url
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('home', views.home, name='home'),
    url('logs', views.logs, name='logs'),
    url('api/messages', views.messages, name = 'messages')
]