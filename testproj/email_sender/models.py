# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserMessage(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	to = models.EmailField()
	delivered = models.BooleanField('was delivered')
	date = models.DateTimeField('date sended')

	def __str__(self):
		return "Sended by %s from %s to %s at %s (Delivered: %s)" % (self.author.username, self.author.email, self.to, self.date.strftime('%c'), self.delivered)