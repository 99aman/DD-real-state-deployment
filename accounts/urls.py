from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^login/$',views.Login,name='login'),
    url(r'^register/$',views.Register,name='register'),
    url(r'^logout/$',views.Logout,name='logout'),
    url(r'^dash/$',views.Dashboard,name='dashboard'),
]
