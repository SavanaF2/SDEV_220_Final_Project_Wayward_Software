from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.
def post_list(request):
    return render(request, 'wayward_software/index.html', {})

def index(request):
    return render(request,'index.html')   

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")