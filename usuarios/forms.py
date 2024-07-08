from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from usuarios.models import DatosExtra

class NuestroFormularioRegistro(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Repetir Contraseña'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Usuario'}),
        }

class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Apellido'}))
    avatar = forms.ImageField(required=False, widget=forms.FileInput)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']
        help_texts = {
        'email': 'Introduce tu dirección de correo electrónico',
        'first_name': 'Introduce tu nombre',
        'last_name': 'Introduce tu apellido',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Usuario'}),
        }

class DatosExtraForm(ModelForm):
    class Meta:
        model = DatosExtra
        fields = ('avatar',)

class CambiarPassword(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Contraseña actual'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Confirmar nueva contraseña'}))

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {
            'old_password': 'Introduce tu contraseña actual',
            'new_password1': 'Introduce tu nueva contraseña',
            'new_password2': 'Confirma tu nueva contraseña',
        }
