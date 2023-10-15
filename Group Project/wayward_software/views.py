from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .models import Package
from .forms import PackageForm, customForm
from django.contrib.auth import logout
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# This is so people can view the list of packages on the home page 
def post_list(request):
	if request.method == "POST":
		  
		product_id = request.POST.get("product_pk")
		package = Package.objects.get(id = product_id)
		request.user.clientprofile.packages.add(package)
		messages.success(request,(f'{package} added to subscriptions.'))
	packages = Package.objects.all()
	user = request.user
	is_employee = user.is_superuser or user.groups.filter(name='Employees').exists()
	return render(request, 'wayward_software/index.html', { "packages":packages, "is_employee": is_employee})
	

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("../")

#This is for the edit profile forum located on client.html
@login_required(login_url='../login')
def client(request):
	if request.method == "POST":

		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.clientprofile)
		if user_form.is_valid():
			user_form.save()
			messages.success(request,('Your profile was successfully updated!'))
		elif profile_form.is_valid():
			profile_form.save()
			messages.success(request,('Your wishlist was successfully updated!'))
		else:
			messages.error(request,('Unable to complete request'))
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.clientprofile)
	user = request.user
	is_employee = user.is_superuser or user.groups.filter(name='Employees').exists()
	return render (request=request, template_name="wayward_software/user.html", context={"user":request.user, "user_form":user_form, "profile_form": profile_form, "is_employee": is_employee})

#enables the user to unsubscribe from packages
@login_required(login_url='../login')
def unsubscribe(request):
	if request.method == "POST":
		profile_form = ProfileForm(request.POST, instance=request.user.clientprofile)
		if profile_form.is_valid():
			profile_form.save()
		product_id = request.POST.get("remove_pk")
		package = Package.objects.get(id = product_id)
		request.user.clientprofile.packages.remove(package)
	profile_form = ProfileForm(instance=request.user.clientprofile)
	return render (request=request, template_name="wayward_software/edit_subscriptions.html", context={"user":request.user, "profile_form": profile_form})

#user can only see the employee page if logged in
@login_required(login_url='../login')

@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Employees').exists())
def employee_view(request):
	if request.method == "POST":
		#enables employees to delete packages
		delete_package_id = request.POST.get("delete_pk")
		Package.objects.filter(id=delete_package_id).delete()
		update_package_id = request.POST.get("update_pk")
		Package.objects.filter(id=update_package_id).update()
		#form that enables employee to add a new software package
		
		add_form = PackageForm(request.POST)
		if add_form.is_valid():
			add_form.save()
	packages = Package.objects.all()
	add_form = PackageForm
	show_clients = User.objects.filter(groups__name='Clients')
	return render(request, 'wayward_software/employee.html', { "packages":packages, "add_form":add_form})

@login_required(login_url='../login')
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Employees').exists())
#enables employees to update packages
def update_view(request, id):
	if request.method == "POST":
		obj = get_object_or_404(Package, id = id)
	
		form = PackageForm(request.POST or None, instance = obj)
	
		if form.is_valid():
			form.save()
			redirect("/employee")
	form = PackageForm
	return render(request, "wayward_software/update_view.html", { "form":form })

@login_required(login_url='../login')
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Employees').exists())
#Shows the list of clients
def client_list(request):
    # Get the "Clients" group
    clients_group = Group.objects.get(name='Clients')

    # Get users belonging to the "Clients" group
    clients = clients_group.user_set.all()

    return render(request, 'wayward_software/clients_list.html', {'clients': clients})

#allow users to make custom software requests
def custom_request(request):
	if request.method == 'POST':
		form = customForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("../")
      
	form = customForm()
	return render(request, "wayward_software/custom_request.html", {'form':form})