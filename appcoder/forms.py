from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class CursoFormulario(forms.Form):

    nombre = forms.CharField()
    camada = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido") #si no quiero q se vea como last_name
    first_name = forms.CharField(label="Nombre") #lo mismo aca
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ["username", "email", "last_name", "first_name", "password1", "password2"]
        

class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido") #si no quiero q se vea como last_name
    first_name = forms.CharField(label="Nombre") #lo mismo aca
    email = forms.EmailField(label="Correo electronico")

    class Meta:
        model = User
        fields = ["email", "last_name", "first_name"]
        
        # ? la siguiente linea elilmina cualquier mensaje dew ayuda en los campos
        # ?help_texts = { k: "" for k in fields }
        help_texts = { "email": "Indica un correco electronico", "first_name": "","last_name":""}