from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#class User(AbstractUser):
#    username = models.CharField(max_length=255, default='')
#    email = models.EmailField(('email address'), unique = True)
#    password = models.CharField(max_length=255)
#    USERNAME_FIELD = 'email' 
#   REQUIRED_FIELDS = []
    
    
class listing(models.Model):
    
    Title=models.CharField(max_length=30)
    Description=models.CharField(max_length=200)
    Images=models.ImageField(upload_to='images/')
    Make=models.CharField(max_length=200)
    CarModel=models.CharField(max_length=200)
    Year=models.IntegerField(default=0)
    Odometer=models.IntegerField(default=0)
    BodyStyle=models.CharField(max_length=200)
    Transmission=models.CharField(max_length=200)
    FuelType=models.CharField(max_length=200)
    EngineSize=models.DecimalField(default=0,decimal_places=2, max_digits=5)
    DriveType=models.CharField(max_length=200)
    ExteriorColor=models.CharField(max_length=200)
    Doors=models.IntegerField(default=0)
    New=models.BooleanField()
    Price=models.DecimalField(default=0, decimal_places=2, max_digits=9)
    WOF=models.BooleanField()
    Registration=models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Title
