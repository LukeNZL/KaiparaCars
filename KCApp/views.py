from django.shortcuts import render, get_object_or_404, redirect
from .forms import ListingForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render 
from .models import listing
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from .serializers import ListingSerializer, RegistrationSerializer, UserLoginSerializer, UserSerializer
from rest_framework import viewsets, status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
import stripe

# Create your views here.

class ListingsList(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
   
   
   
    queryset = listing.objects.order_by('created')
    serializer_class=ListingSerializer
    
    
    
    
    #def create(self, request):
    #    file_uploaded = request.FILES.get('file_uploaded')
    #    content_type = file_uploaded.content_type
    #    response = "POST API and you have uploaded a {} file".format(content_type)
    #    return Response(response)
class UserRegistration(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        print("hellow")
        print(request.data)
        data=request.data
        serializer=RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.create(data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
            
           
class UserLogin(APIView):  
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    headers={'Access-Control-Allow-Origin':'*', 'Access-Control-Expose-Headers':'*'}
    def post(self, request):
        data=request.data
        serializer=UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.login_user(data)
            if user:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)
 
class UserView(APIView):  
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        user=request.user
        serializer=UserSerializer(user)
        return Response({'user':serializer.data}, status=status.HTTP_200_OK)

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
stripe.api_key = "sk_test_51MyNtpHWI00ENRWp3WaxRiGRLsD2HUnlt30BBCXXck5OnFTdDZ5LDU9V422Owy0MPeXVa3MJz35djreUB42429Tm00S9ylQUwp"
MY_DOMAIN = "https://www.kaiparacars.com"
def create_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '1000',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=MY_DOMAIN + '?success=true',
            cancel_url=MY_DOMAIN + '?canceled=true',
        )
    except Exception as e:
        return HttpResponse(str(e))
    
    return HttpResponseRedirect(checkout_session.url)

    
      
def LandingPage(request):
    return render(request, 'LandingPage.html')

def Listings(request):
    
    ListingList = listing.objects.order_by('created')
    #print(ListingList)
    
    #model_search = listing.objects.values_list('CarModel', flat=True).distinct()
    #year_search = listing.objects.values_list('Year', flat=True).distinct()
    #make_search = listing.objects.values_list('Make', flat=True).distinct()
    #transmission_search = listing.objects.values_list('Transmission', flat=True).distinct()
    #make_search = listing.objects.values_list('Make', flat=True).distinct()
    
    
    
    context = {'ListingList': ListingList,
               #'model_search': model_search,
               #'year_search': year_search,
               #'make_search': make_search,
               #'transmission_search': transmission_search
               }
    
    return render(request, 'Listings.html', context)

def NewListing(request):
    form=ListingForm()
    

    #cat_id = request.GET.get('cat_id')
    #if cat_id is not None:
    #    category = get_object_or_404(listing, id=cat_id)
    #    data = category.objects.all()
    #    print (data)
    #    print (data.all())
        
   # else:
   #     return HttpResponseBadRequest()
    #print(form)
    if request.method == 'POST':
        form=ListingForm(request.POST, request.FILES)
        print(form.data)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.CreatedBy = request.user
            new_listing.save()
        else:
            print("An error occurred during listing creation (2)")
            messages.error(request, 'An error occurred during listing creation (2)')
        
       
        
        
    return render(request, 'NewListing.html')

def ViewListing(request, listing_id):
    
    ViewListing = get_object_or_404(listing, id=listing_id)
    print(ViewListing.CloudImage.url)
    if ViewListing.CreatedBy == request.user.username:
        print("this is my listing")
        mylisting=True
    else:
        print("this is not my listing")
        mylisting=False

    context = {'ViewListing': ViewListing,
               'mylisting': mylisting,
               'listing_id': listing_id}
    return render(request, 'ViewListing.html', context)
    
def EditListing(request, listing_id):
    EditListing = get_object_or_404(listing, id=listing_id)
    form=ListingForm(instance=EditListing)
    
    if request.method == 'POST':
        form=ListingForm(request.POST, request.FILES, instance=EditListing)
        print(form.data)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            EditListing = form.save(commit=False)
            EditListing.save()
            
            return redirect('viewlisting', listing_id=listing_id)
        else:
            print("An error occurred during listing creation (2)")
            messages.error(request, 'An error occurred during listing creation (2)')
        
       
        
        
    return render(request, 'EditListing.html', {'form': form})    
def DeleteListing(request, listing_id):
    listing_to_delete = get_object_or_404(listing, id=listing_id)
    
    if request.method == 'POST':
        listing_to_delete.delete()
        print("deleted listing")
        return redirect('mylistings')
    return render(request, 'DeleteListing.html')
    

  
   

def MyListing(request):
    c= request.user
    #MyListings = listing.objects.get( "CreatedBy" ==c)
    MyListings = listing.objects.all()
    MyListings = MyListings.filter(CreatedBy=c)
    
    #print(MyListings)
    
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
            #username = request.POST.get('username').lower()
            password = request.POST.get('password')
            email= request.POST.get('email').lower()
            try:
                user = User.objects.get(email=email)
            except:
                messages.error(request, 'User does not exist')
            #user = authenticate(request, email=email, password=password)
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