from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# def login(request):
#     # return HttpResponse("Inicio")}
#     return render(request, 'Autenticacion/login.html')

class vista_resgistro(View):

    # definimos la funcionalidad de los dos methodos

    def get(self, request):
        form = UserCreationForm()
        return render(request, "Autenticacion/registro.html", {"form":form})
    
    def post(self, request):
        # para usar el formulario de django para crear usuario (ya estan enlazados con la base de datos)
        form = UserCreationForm(request.POST)

        if form.is_valid():

            usuario = form.save()
            login(request, usuario)
            return(redirect('inicio'))
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "Autenticacion/registro.html", {"form":form})

def cerrar_login(request):

    # los usamos para cerrar session
    logout(request)

    return redirect('inicio')

def Login(request):

    if request.method == "POST":
        # formulario de django para hacer login
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                for msg in form.error_messages:
                    # usamos e iteramos por lo mensajes (de error que manda el formulario de django)
                    messages.error(request, form.error_messages[msg])
                    return render(request, "Autenticacion/login.html", {"form":form})
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                return render(request, "Autenticacion/registro.html", {"form":form})



    form = AuthenticationForm()
    return render(request, "Autenticacion/login.html", {"form":form})
            