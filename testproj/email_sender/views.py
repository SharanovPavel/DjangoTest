# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from .models import UserMessage
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def mail_admins(request):
	if request.method == 'POST':
		admin_emails = [v for k,v in settings.ADMINS]
		form = ContactForm(request.POST)
		user = request.user
		if form.is_valid():
			text = form.cleaned_data['text']
			to = form.cleaned_data['to']
			record = UserMessage(author = user, text = text, to = to, delivered = False, date = timezone.now())
			if(to in admin_emails):
				res = send_mail('Django Test App: %s want to tell you something!' % (user.username), text, user.email, [to,], fail_silently=True)
				if res > 0:
					record.delivered = True
			record.save()
			return render(request, 'done.html')
	else:
		form = ContactForm()
	return render(request, 'contact_form.html', {'form': form.as_p()})