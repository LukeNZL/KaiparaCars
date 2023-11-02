from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPage, name='landingpage'),
    path('listings/', views.Listings, name='listings'),
    path('newlisting/', views.NewListing, name='newlisting'),
<<<<<<< HEAD
    path('viewlisting/', views.ViewListing, name='viewlisting'),
    path('login/', views.login, name='login'),
    
]
=======
    path('listing_<int:listing_id>/', views.ViewListing, name='viewlisting'),
    path('myaccount/', views.Accounts, name='myaccount'),
    path('logout/', views.logoutUser, name='logout'),
    path('mylistings/', views.MyListing, name='mylistings'),
    path('deletelisting/<int:listing_id>/', views.DeleteListing, name='deletelisting'),
    path('editlisting/<int:listing_id>/', views.EditListing, name='editlisting'),
 
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> ed9a03c2eec65ca895d10157fdf1a2e59707d487
