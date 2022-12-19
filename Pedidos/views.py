from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppCarro.models import Carro
from Pedidos.models import Pedidos, ListaPedidos
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

#  Un decorador para que al momento de ejecutar esta funcion/vista, el usuario debe estar loggueado
@login_required(login_url="/Registro/Login")

def procesar_pedido(request):
    # creamo un pediodo pasando datos del usuario loggueado
    pedido = Pedidos.objects.create(user =  request.user)
    carro = Carro(request)
    lineas_pedido = list()
    # de los items del carrito se lo pasamos a lista pedidos para luego crearla en la base de datos
    for key, value in carro.carro.items():
        lineas_pedido.append(ListaPedidos(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))

    # usamos bulk para esto
    ListaPedidos.objects.bulk_create(lineas_pedido)

    enviar_email(
        pedido = pedido,
        lineas_pedido =  lineas_pedido,
        nombreusuario = request.user.username,
        emailusuario = request.user.email
    )


    return redirect("../AppTienda/tienda")


def enviar_email(**kwars):
    asunto = "Gracias Por Hacer El Pedido!"
    # usuams render_to_string para tener como templet un archivo html
    mensaje =  render_to_string("Pedidos/email.html",{
        "pedido":kwars.get("pedido"),
        "lineas_pedido": kwars.get("lineas_pedido"),
        "nombreusuario": kwars.get("nombreusuario")
    })

    # Usamos strips tags para que solo me mietre lo del body sin las etiquetas del html
    mensaje_texto = strip_tags(mensaje)
    from_email = "proyectoweb@srrobls.com"
    # to = kwars.get("emailusuario")
    to = "johanrobles600@gmail.com" #cambiar cuenta para que llegue a tu correo
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

