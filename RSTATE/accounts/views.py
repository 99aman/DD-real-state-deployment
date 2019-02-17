from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.

def Register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'This username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This email is already exists.')
                    return redirect('register')
                #Every things Look Good than create User
                else:
                    user=User.objects.create_user(first_name=first_name,last_name=last_name, username=username,email=email,password=password)
                    user.save()
                    messages.success(request,'You are register please log in now.')
                    return redirect('login')
        else:
            messages.error(request,'password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/registration.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in.')
            return redirect('listings')
        else:
            messages.error(request,'Wrong credential')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are log out')
        return redirect('about')

def Dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contact':user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)
