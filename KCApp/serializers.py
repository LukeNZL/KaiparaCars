from rest_framework import serializers
from .models import *

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields = ['id','Title', "Description","Price","CloudImage"]
        