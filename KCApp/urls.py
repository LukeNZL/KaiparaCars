from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPage, name='landingpage'),
    path('listings/', views.Listings, name='listings'),
    path('newlisting/', views.NewListing, name='newlisting'),
    path('listing_<int:listing_id>/', views.ViewListing, name='viewlisting'),
    path('myaccount/', views.Accounts, name='myaccount'),
    path('logout/', views.logoutUser, name='logout'),
    path('mylistings/', views.MyListing, name='mylistings'),
    path('deletelisting/<int:listing_id>/', views.DeleteListing, name='deletelisting'),
    path('editlisting/<int:listing_id>/', views.EditListing, name='editlisting'),
    
    #userapi paths
    path('register', views.UserRegistration.as_view(), name='register'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('user', views.UserView.as_view(), name='user'),
    path('userlist', views.UserList.as_view(), name='userlist'),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
