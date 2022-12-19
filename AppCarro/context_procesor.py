# Creamos un context_procesor, que basicamnete, para cada session se genera una serie de argumentos
# en la cual cargaran datos distintos dependiendo de cada session y podremos acceder a ellos de manera global.

# Importante: debemos registrar es archivo en settings

def cargar_total_carrito(request):
    total = 0
    # verificamos se un usuario esta autenticado
    # if request.user.is_authenticated:
    if "carro" in request.session:
            for key, value in request.session["carro"].items():
                total = total +  float(value["precio"])
    
    return {"cargar_total_carrito": total}