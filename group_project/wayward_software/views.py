from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'wayward_software/index.html', {})

def index(request):
    return render(request,'index.html')   
def sign_up(request):
    # Your sign-up logic here
    return render(request, 'wayward_software/sign_up.html')
def login(request):
    # Your login logic here
    return render(request, 'wayward_software/login.html')
