from django.shortcuts import render
from .forms import ListingForm
# Create your views here.

def LandingPage(request):
    return render(request, 'LandingPage.html')

def Listings(request):
    return render(request, 'Listings.html')

def NewListing(request):
    form=ListingForm()
    context = {}
    context['form']=form
    return render(request, 'NewListing.html',context)

def ViewListing(request):
    return render(request, 'ViewListing.html')

def login(request):
    return render(request, 'login.html')
