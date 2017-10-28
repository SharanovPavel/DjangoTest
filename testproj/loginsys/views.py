# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from .forms import AuthenticationFormWithInactiveUsersOkay, UserCreationFormWithEmail
# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		is_authenticated = user is not None
		data = {'success': is_authenticated}
		if is_authenticated:
			auth.login(request, user)
		return JsonResponse(data)
	else:
		form = AuthenticationFormWithInactiveUsersOkay()
	return render(request, 'login.html', {'form': form.as_p() })

def logout(request):
	auth.logout(request)
	return redirect('index')

def register(request):
	if request.method == 'POST':
		form = UserCreationFormWithEmail(request.POST)
		data = {'success': form.is_valid()}
		if (data['success']):
			form.save()
		return JsonResponse(data)
	else:
		form = UserCreationFormWithEmail()
	return render(request, 'register.html', {'form': form.as_p() })