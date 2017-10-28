from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

class UserCreationFormWithEmail(UserCreationForm):
	email = forms.EmailField()