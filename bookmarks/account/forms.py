# Importamos el módulo 'forms' de Django, que se utiliza para crear formularios web.
from django import forms

# Definimos la clase 'LoginForm', que hereda de 'forms.Form'. Esta clase representa un formulario de inicio de sesión.
class LoginForm(forms.Form):
    # Definimos un campo de texto llamado 'username'. Este campo es obligatorio por defecto.
    username = forms.CharField()
    
    # Definimos un campo de texto llamado 'password'. Usamos el widget 'forms.PasswordInput' para que el campo sea de tipo contraseña (los caracteres se mostrarán como asteriscos).
    password = forms.CharField(widget=forms.PasswordInput)
