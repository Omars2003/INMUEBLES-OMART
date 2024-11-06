from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Importamos el formulario de inicio de sesión previamente definido.
from .forms import LoginForm

# Definimos la vista 'user_login' que maneja el inicio de sesión del usuario.
def user_login(request):
    # Verificamos si la solicitud es de tipo POST (es decir, si se enviaron datos a través del formulario).
    if request.method == 'POST':
        # Creamos una instancia de 'LoginForm' con los datos proporcionados por el usuario.
        form = LoginForm(request.POST)
        # Verificamos si el formulario es válido.
        if form.is_valid():
            # Obtenemos los datos limpios del formulario.
            cd = form.cleaned_data
            # Autenticamos al usuario utilizando el nombre de usuario y la contraseña proporcionados.
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'],
            )

            if user is not None:
                # Verificamos si la cuenta del usuario está activa.
                if user.is_active:
                    # Iniciamos la sesión del usuario.
                    login(request, user)
                    # Retornamos una respuesta indicando que la autenticación fue exitosa.
                    return HttpResponse('Authenticated successfully')
                else:
                    # Retornamos una respuesta indicando que la cuenta está deshabilitada.
                    return HttpResponse('Disabled account')
            else:
                # Retornamos una respuesta indicando que las credenciales son inválidas.
                return HttpResponse('Invalid login')
    else:
        # Si la solicitud no es de tipo POST, creamos un formulario vacío.
        form = LoginForm()
    # Renderizamos la plantilla 'account/login.html' con el formulario.
    return render(request, 'account/login.html', {'form': form})