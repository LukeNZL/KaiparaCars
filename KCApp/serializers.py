from rest_framework import serializers
from .models import *
from rest_framework.response import Response
from rest_framework import status

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields = ['id','Title', "Description","Price","CloudImage"]
        
        
   
        