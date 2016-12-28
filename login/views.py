from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.forms import *
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext


from .forms import RegistrationForm
def register(request):
	if request.method == 'POST':
		form  = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password'])
			return HttpResponseRedirect('/register/success')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {}
	)	
	return render(request, 'registration/register.html', {'form':form})			

def register_success(request):
	return render(request, 'registration/success.html')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def home(request):
	return render(request,
	'home.html',
	{ 'user': request.user}	
)
