from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        user_id = request.POST['user_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id=request.user.id
            contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if contacted:
                messages.error(request,'You already make inquiry for this home')
                return redirect('/listing/'+listing_id)

        contact = Contact(user_id=user_id,listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,message=message)
        contact.save()
        messages.success(request,'Thanks for inquiry.The realtor will touch you soon.')
        return redirect('dashboard')
