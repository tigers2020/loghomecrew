from ckeditor.widgets import CKEditorWidget
from django import forms


class ContactForm(forms.Form):
	first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control input_box'}))
	last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control input_box'}))
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'E-Mail', 'class': 'form-control input_box'}))
	subject = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control input_box'}))
	message = forms.CharField(label='', widget=CKEditorWidget(attrs={'placeholder': 'Message', 'class': 'form-control input_box'}))
