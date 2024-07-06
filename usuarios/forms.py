from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

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
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {
        'email': 'Introduce tu dirección de correo electrónico',
        'first_name': 'Introduce tu nombre',
        'last_name': 'Introduce tu apellido',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Usuario'}),
        }

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class NuestroFormularioRegistro(UserCreationForm):
#     email = forms.EmailField
#     password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         help_texts = {key: '' for key in fields}