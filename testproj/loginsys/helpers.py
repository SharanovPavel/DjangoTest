# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib.auth.models import User

def authenticate_user(username, password):
	return auth.authenticate(username=username, password=password)
	

def login_user(request, username, password):
	print "Logging in with %s:%s" % (username, password)
	user = authenticate_user
	success = user is not None
	if success:
		auth.login(user)
	return success
