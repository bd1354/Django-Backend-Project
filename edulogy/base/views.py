from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from store.models import *
from store.utils import cookieCart, cartData, guestOrder


from .forms import CreateUserForm

# Create your views here.

def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
     
    return render(request, 'home.html',context)

def blog(request):
    return render(request, 'blog.html')

def blog1(request):
    return render(request, 'blog-1.html')

def blog2(request):
    return render(request, 'blog-2.html')

def blog3(request):
    blogs = BlogModel.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    
    context= {
        'blogs':blogs,
        'cartItems':cartItems
    }
    return render(request, 'blog-3.html',context)

def blogsingle(request,id):
   
    obj = BlogModel.objects.get(pk=id)
    data = cartData(request)
    cartItems = data['cartItems']
    suggestBlogs = BlogModel.objects.order_by('?')

    context = {'obj': obj,'cartItems':cartItems,'suggestBlogs':suggestBlogs}

    return render(request, 'blog-single.html',context)

def storesingle(request,id):
    product = Product.objects.get(pk=id)
    data = cartData(request)
    cartItems = data['cartItems']
    suggestProducts = Product.objects.order_by('?')

    context = {'product': product,'cartItems':cartItems,'suggestProducts':suggestProducts}

    return render(request, 'shop-single.html',context)

def events(request):

    data = cartData(request)
    cartItems = data['cartItems']
    
    context = {'cartItems':cartItems}
    products = Product.objects.all() 

    return render(request, 'events.html',context)

def pagecontact(request):
    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems':cartItems}

    return render(request, 'page-contact.html',context)

def readmore(request):
    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems':cartItems}

    return render(request, 'readmore.html',context)


def shopsingle(request):
    return render(request, 'shop-single.html')

def shop(request):
    inventory = Inventory.objects.all()
    context= {
        'inventory':inventory
    }
    return render(request, 'shop.html',context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' +user)
            return redirect('login')
            #Kullanici kayit oldugunda otomatik olarak login edilmesi icin redirect kullaniliyor

    context = {'form' : form}
    return render(request,'register.html',context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Product.objects.filter(name__contains=searched)
    
        return render(request, 
        'search_venues.html', 
        {'searched':searched,
        'venues':venues})
    else:
        return render(request, 
        'search_venues.html', 
        {})

