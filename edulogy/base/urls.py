from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html/', views.home, name='home'),  
    path('blog.html/', views.blog, name="blog"),
    path('blog-1.html/', views.blog1, name="blog1"),
    path('blog-2.html/', views.blog2, name="blog2"),
    path('blog-3.html/', views.blog3, name="blog3"),
    path('blog-single.html/<int:id>', views.blogsingle, name="blogsingle"),
    path('events.html/', views.events, name="events"),
    path('page-contact.html/', views.pagecontact, name="pagecontact"),
    path('readmore.html/', views.readmore, name="readmore"),

    path('register.html/', views.registerPage, name="register"),
    path('login.html/', views.loginPage, name="login"),
    path('logout.html/', views.loginPage, name="logout"),
    
    path('shop-single.html/<int:id>',views.storesingle,name='storesingle'),
    
    path('search_venues', views.search_venues, name='search-venues'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)