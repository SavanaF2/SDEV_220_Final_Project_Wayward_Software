from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    #creates the email field for the register.html page
    email = forms.EmailField()

    class Meta:
        model = User
        #This controls which fields show up and the order that they show up in
        fields = ["username", "email", "password1", "password2"]