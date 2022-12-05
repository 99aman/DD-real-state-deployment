from django.shortcuts import render
from listings.models import Listing
from listings.choices import bedroom_choices,state_choices,price_choices
from realtors import models

# Create your views here.
def About(request):
    list_name = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    state_name=state_choices.items
    bedroom=bedroom_choices.items
    price=price_choices.items
    context={'listing':list_name,'st':state_name,'bedroom':bedroom,'price':price}
    return render(request,'DDstate/about.html',context)

def Index(request):
    realtor=models.Realtor.objects.order_by('hire_date')
    #sofm(Seller of the month)
    sofm=models.Realtor.objects.all().filter(is_mvp=True)
    context={'realtors_name':realtor,'seller_of_M':sofm}

    return render(request,'DDstate/index.html',context)
