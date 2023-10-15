from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    #creates the email field for the register.html page
    email = forms.EmailField()
    class Meta:
        model = User
        #This controls which fields show up and the order that they show up in
        fields = ["username", "email", 'first_name', 'last_name',"password1", "password2"]

class EmployeeRegistrationForm(UserCreationForm):
    job_title = forms.CharField(max_length=100)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username",'first_name','last_name','email', 'job_title', 'password1', 'password2')

    def save(self, commit=True):
        employee = super(EmployeeRegistrationForm, self).save(commit=False)
        employee.job_title = self.cleaned_data['job_title']
        if commit:
            employee.save()
        return employee

