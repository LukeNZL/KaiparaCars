from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import listing, listingcatagory
# custom form built off of prebuilt django form
class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=4, max_length=150)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    email = forms.EmailField(label='email', max_length=150)
    # makes all characters lowercase so users can't make duplicate accounts with different capitalisations.
    # also, then checks username with names already in the database
    # these functions validate the form when the corresponding function is called in the views file
    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username
    
    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            #None,
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
    
class ListingForm(ModelForm):
    category = forms.ModelChoiceField(queryset=listingcatagory.objects.all(), required=False)

    class Meta:
        model = listing
        fields = [
            
            'Title',
            'Description',
            #'Images',
            'CloudImage',
            #'Make',
            #'CarModel',
            #'Year',
            #'Odometer',
            #'BodyStyle',
            #'Transmission',
            #'FuelType',
            #'EngineSize',
            #'DriveType',
            #'ExteriorColor',
            #'Doors',
            #'New',
            'Price',
            #'WOF',
            #'Registration',
                    
            
        ]
    