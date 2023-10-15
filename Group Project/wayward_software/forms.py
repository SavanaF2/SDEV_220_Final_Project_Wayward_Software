from .models import clientProfile, Package
from django.contrib.auth.models import User
from django import forms
#imports clientProfile from wayward_software models.py

#Allows users to edit their profile information
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

#allows users to edit their packages
class ProfileForm(forms.ModelForm):
	class Meta: 
		model = clientProfile
		fields = ('packages',)
            
#allows imployees to edit packages
class PackageForm(forms.ModelForm):
    
    class Meta:
        model = Package
        fields = ("package_name", "description", "subscription_price")

class customForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)