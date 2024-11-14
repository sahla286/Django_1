from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}))
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']