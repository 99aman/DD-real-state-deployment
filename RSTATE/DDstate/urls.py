from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.About,name='about'),
    url(r'^index/$',views.Index,name='index'),
]
