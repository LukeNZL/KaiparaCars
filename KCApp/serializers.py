from rest_framework import serializers
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

UserModel=User


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields = ['id','Title', "Description","Price","CloudImage"]

class LS(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields = ['id','Title', 'Description','Price','CloudImage']
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields='__all__'

    def create(self, cleaned_data):
        print(cleaned_data)
        user=UserModel.objects.create_user(
            username=cleaned_data['username'].lower(),
            email=cleaned_data['email'].lower(),
            password=cleaned_data['password']
        )
        user.save()
        return user
    
    
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=('email','password')
        
    email=serializers.EmailField()
    password=serializers.CharField()
    
    def login_user(self, cleaned_data):#maybe add variables in auth function
        user = User.objects.filter(email=cleaned_data['email']).first()
        if not user:
            raise serializers.ValidationError("sorry, user not found")
        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=('email','username')

   
        