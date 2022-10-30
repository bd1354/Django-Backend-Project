from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name='home'),
    path('blog.html', views.blog, name="blog"),
    path('blog-1.html', views.blog1, name="blog1"),
    path('blog-2.html', views.blog2, name="blog2"),
    path('blog-3.html', views.blog3, name="blog3"),
    path('blog-single.html', views.blogsingle, name="blogsingle"),
    path('events.html', views.events, name="events"),
    path('page-contact.html', views.pagecontact, name="pagecontact"),
    path('shop-single.html', views.shopsingle, name="shopsingle"),
    path('shop.html', views.shop, name="shop"),
    
]