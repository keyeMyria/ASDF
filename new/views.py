from django.shortcuts import render,redirect
from new.forms import RegistrationForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Creat e your views here.
def register(request):
	if request.method=='POST':
		form =RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/new/login')
	else:
		form = RegistrationForm()
	args = {'form':form}
	return render(request,'new/reg_form.html',args)

@login_required
def view_profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user

	args = {'user':user}
	return render(request,'new/profile.html',args)

@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/new/profile/')
		else:
			return redirect('/new/profile/edit/')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form':form}
		return render(request ,'new/edit_profile.html',args)
		
@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/new/profile/change_password')
		else:
			return redirect('/new/profile/')
	else:
		form = PasswordChangeForm(user=request.user)
	args = {'form':form}
	return render(request ,'new/changepass.html',args)
