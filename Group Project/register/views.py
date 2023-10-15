from django.shortcuts import render, redirect
from .forms import RegisterForm, EmployeeRegistrationForm
from django.contrib.auth import login, authenticate #import authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #import AuthenticationForm
from django.contrib.auth.models import Group

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"form":form})

# Enables regular users and employees to register
def register(request):
	if request.method == "POST":
		#If the user is staff they see the form to register an employee
		if request.user.is_superuser or request.user.groups.filter(name='Employees').exists():
			form = EmployeeRegistrationForm(request.POST)
		#If it's just a regular user they see the user registration form instead
		else:
			form = RegisterForm(request.POST)

		if form.is_valid():
				#Saves the form for the employees and adds the new employee to a group called Employees
				if request.user.is_superuser or request.user.groups.filter(name='Employees').exists():
					emp = form.save()
					group = Group.objects.get(name='Employees')
					emp.groups.add(group)
				#Saves the form for the user and adds the new user to a group called Clients
				else:
					client = form.save()
					group = Group.objects.get(name='Clients')
					client.groups.add(group)
					login(request, client)
				return redirect("../")
	
	else:
		if request.user.is_superuser or request.user.groups.filter(name='Employees').exists():
			form = EmployeeRegistrationForm
		else:
			form = RegisterForm

	user = request.user
	is_employee = user.is_superuser or user.groups.filter(name='Employees').exists()
	return render(request, "register/register.html", {"form":form, "is_employee":is_employee})


