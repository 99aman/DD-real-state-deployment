from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.Index,name='listings'),
    url(r'^(?P<listing_id>[0-9])/$',views.Listing,name='listing'),
    url(r'^search/$',views.Search,name='search'),
]
