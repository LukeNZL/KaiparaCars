from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPage, name='landingpage'),
    path('listings/', views.Listings, name='listings'),
    path('newlisting/', views.NewListing, name='newlisting'),
    path('listing_<int:listing_id>/', views.ViewListing, name='viewlisting'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    
]
