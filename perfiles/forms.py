from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class Editar_Perfil(ModelForm):

    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email')