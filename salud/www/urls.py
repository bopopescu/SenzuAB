
from django.conf.urls import url, include
from . import views

urlwww = [
    url(r'^api_v1/', 'www.views.index', name='home'),
]