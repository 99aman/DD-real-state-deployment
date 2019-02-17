from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from listings.choices import bedroom_choices,state_choices,price_choices
from . import models
from realtors.models import Realtor
# Create your views here.

def Index(request):
    list = models.Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(list,3)
    page = request.GET.get('page')

    try:
        paged_listings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paged_listings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paged_listings = paginator.page(paginator.num_pages)

    context= {'name_list':paged_listings}
    return render(request, 'listings/listings.html',context)

def Listing(request,listing_id):
    listing=get_object_or_404(models.Listing,pk=listing_id)
    realtor_name=Realtor.objects.all()
    context={'enq_list':listing,'realtor':realtor_name}
    return render(request, 'listings/listing.html',context)

def Search(request):
    queryset_list=models.Listing.objects.order_by('-list_date')

#Keyword
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)


#City
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)
#State
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state)
#Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)
#Price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)


    context={'st':state_choices.items,'bedroom':bedroom_choices.items,
            'price':price_choices.items,'name_list':queryset_list,'values':request.GET}
    return render(request, 'listings/search.html',context)
