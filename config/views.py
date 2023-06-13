#Request: Para realizar peticiones al servidor.
#HttpResponse: Para enviar respuesta usando el protocolo HTTP.
from django.http import HttpResponse

#Esto es una vista
def home(request): #Se pasa un objeto Request como primer argumento
    return HttpResponse("Bienvenido")

def inicio(request):
    return HttpResponse("Ahora si nada")