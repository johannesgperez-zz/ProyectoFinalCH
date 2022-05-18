from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.models import User

class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.EmailField(widget=forms.EmailInput)
    first_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')