from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def blog1(request):
    return render(request, 'blog-1.html')

def blog2(request):
    return render(request, 'blog-2.html')

def blog3(request):
    return render(request, 'blog-3.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def events(request):
    return render(request, 'events.html')

def pagecontact(request):
    return render(request, 'page-contact.html')

def shopsingle(request):
    return render(request, 'shop-single.html')

def shop(request):
    return render(request, 'shop.html')



