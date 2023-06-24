from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id' : 'usertxtreg'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'emailtxtreg'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'id' : 'passtxtreg'}),
        label='Ingrese Contraseña'
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'id' : 'passtxtreg'}),
        label='Vuelva a escribir la contraseña'
        )
    is_staff = forms.BooleanField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff', )

class loginForm(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password',)
