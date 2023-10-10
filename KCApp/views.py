from django.shortcuts import render, get_object_or_404, redirect
from .forms import ListingForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render 
from .models import listing
# Create your views here.

def LandingPage(request):
    return render(request, 'LandingPage.html')

def Listings(request):
    
    ListingList = listing.objects.order_by('created')
    
    print(ListingList)
    
    context = {'ListingList': ListingList}
    return render(request, 'Listings.html', context)

def NewListing(request):
    form=ListingForm()
    
    if request.method == 'POST':
        form=ListingForm(request.POST, request.FILES)
        print(form.data)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            #form["CreatedBy"] = request.user
            new_listing = form.save(commit=False)
            new_listing.CreatedBy = request.user
            new_listing.save()
        else:
            print("An error occurred during listing creation (2)")
            messages.error(request, 'An error occurred during listing creation (2)')
        
       
        
        
    return render(request, 'NewListing.html')

def ViewListing(request, listing_id):
    
    #ViewListing = listing.objects.get(listing, id=listing_id)
    ViewListing = get_object_or_404(listing, id=listing_id)
    #print(ViewListing)
    #print(ViewListing.Description)
    context = {'ViewListing': ViewListing}
    return render(request, 'ViewListing.html', context)

def MyListing(request):
    c= request.user
    #MyListings = listing.objects.get( "CreatedBy" ==c)
    MyListings = listing.objects.all()
    MyListings = MyListings.filter(CreatedBy=c)
    
    print(MyListings)
       
    context = {'MyListings': MyListings}
    return render(request, 'MyListings.html', context)

def Accounts(request):
    ## login ##
    #form = RegisterForm()

    if request.method == 'POST':
        if "register" in request.POST:  # add the name "register" in your html button
            form = RegisterForm(request.POST)
            print(form.data)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.email = user.email.lower()
                user.save()
                login(request, user)
            else:
                messages.error(request, 'An error occurred during registration (1)')

        if "login" in request.POST:  # add the name "login" in your html button
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'User does not exist')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                messages.error(request, 'Username or password does not exist')
    return render(request, 'AccountPage.html')
    ## login ##

def logoutUser(request):
    logout(request)
    return redirect('myaccount')

#beckend todo: mylistings page with crud functionality
#accounts page with crud functionality
#search functionality
#Catagories
#Stripe