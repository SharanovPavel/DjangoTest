from django import forms

class ContactForm(forms.Form):
	to = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)