from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#class user(AbstractUser):
#    username = models.CharField(max_length=255, default='')
#    email = models.CharField(max_length=255, unique=True)
#    password = models.CharField(max_length=255)
#    USERNAME_FIELD = 'email' 
#    REQUIRED_FIELDS = []
    
    
class listing(models.Model):
    
    Title=models.CharField(max_length=30, null=True)
    Description=models.CharField(max_length=200, null=True)
    Images=models.ImageField(upload_to='images/', null=True)
    Make=models.CharField(max_length=200, null=True)
    CarModel=models.CharField(max_length=200, null=True)
    Year=models.IntegerField( null=True)
    Odometer=models.IntegerField( null=True)
    BodyStyle=models.CharField(max_length=200, null=True)
    Transmission=models.CharField(max_length=200, null=True)
    FuelType=models.CharField(max_length=200, null=True)
    EngineSize=models.DecimalField(decimal_places=2, max_digits=5, null=True)
    DriveType=models.CharField(max_length=200, null=True)
    ExteriorColor=models.CharField(max_length=200, null=True)
    Doors=models.IntegerField( null=True)
    New=models.BooleanField( null=True)
    Price=models.DecimalField(decimal_places=2, max_digits=9, null=True)
    WOF=models.BooleanField( null=True)
    Registration=models.BooleanField( null=True)
    created = models.DateTimeField(auto_now_add=True)
    CreatedBy=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.Title
