from django.contrib import admin
from .models import listing, listingcatagory

# Register your models here.
admin.site.register(listing)
admin.site.register(listingcatagory)

