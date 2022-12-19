from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contacto(request):
    # return  HttpResponse("Contacto")
    contacto_form = ContactForm()
    
    if request.method == "POST":
        contacto_form = ContactForm(data=request.POST)
        if contacto_form.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")
        
        # Enviar informacion a correo
        email_mensaje = EmailMessage("Mensaje enviado desde ProyectoWeb Django",
        f"Nombre: {nombre}\nEmail: {email}\n\n {mensaje}","",["johanrobles600@gmail.com"],
        reply_to=[email])

        try:
            email_mensaje.send()
            return redirect('?valido/')
        except:
            return redirect('?invalido/')

    return render(request, 'AppContacto/contacto.html', {"contacto": contacto_form})