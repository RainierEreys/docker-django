#Request: Para realizar peticiones al servidor.
#HttpResponse: Para enviar respuesta usando el protocolo HTTP.
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
import xmlrpc.client

#POO creacion de clase PERSONA
class Persona(object):
    #CONSTRUCTOR QUE RECIBE DOS PARAMETROS 'SELF' SIEMPRE ESTA AHI POR DEFECTO
    def __init__(self, nombre, apellido):
        
        self.nombre = nombre
        self.apellido = apellido
    

#Esto es una vista
def home(request): #Se pasa un objeto Request como primer argumento
    
    #CREACION DE OBJETO DE CLASE PERSONA
    person1 = Persona("Pedro", "Barrios")
    person2 = Persona("Rainier", "Peña")
    
    nombre = 'Rainier'
    apellido = "Peña"
    
    temas_curso = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue de aplicación']
    
    fecha = datetime.datetime.now()
    dia = fecha.day
    mes = fecha.month
    agno = fecha.year
    
    #doc_externo = open("../docker-django/config/templates/home.html")
    
    #plt=Template(doc_externo.read())
    
    #doc_externo.close()
    
    
    #YA SE ESPECIFICO LA RUTA DE LOS TEMPLATES EN EL ARCHIVO SETTINGS, AQUI SOLO SOLICITAMOS EL TEMPLATE CON EL METODO 'get_template()'
    #doc_externo = loader.get_template('home.html')
    #HAY QUE CREAR CONTEXTO SIEMPRE AUNQUE ESTE VACIO
    #Estos diccionarios reciben diccionarios para pasar variables a ll template
    #ctx=Context({"nombre_persona":person2.nombre, "apellido_persona":person2.apellido, "fecha":fecha, "dia":dia, "mes":mes, "agno":agno, "temas":temas_curso})
    
    #doc = doc_externo.render({"nombre_persona":person2.nombre, "apellido_persona":person2.apellido, "fecha":fecha, "dia":dia, "mes":mes, "agno":agno, "temas":temas_curso})
    
    return render(request, 'home.html', {"nombre_persona":person2.nombre, "apellido_persona":person2.apellido, "fecha":fecha, "dia":dia, "mes":mes, "agno":agno, "temas":temas_curso})

def inicio(request):
    
    #CREACION DE OBJETO DE CLASE PERSONA
    person1 = Persona("Pedro", "Barrios")
    person2 = Persona("Rainier", "Peña")
    
    nombre = 'Rainier'
    apellido = "Peña"
    
    temas_curso = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue de aplicación']
    
    fecha = datetime.datetime.now()
    dia = fecha.day
    mes = fecha.month
    agno = fecha.year
    
    return render(request, 'inicio.html', {"nombre_persona":person2.nombre, "apellido_persona":person2.apellido, "fecha":fecha, "dia":dia, "mes":mes, "agno":agno, "temas":temas_curso})


def pasaedad(request, edad, agno):
    
    #edadActual = 22
    periodoprueba = agno - 2023
    edadfutura = edad + periodoprueba
    #%s son marcadores de posicion para agregar variables a la cadena de contenido
    doc = """
    <html>
        <body>
            <h2>En el año %s tendrás %s años</h2>
        </body>
    </html>
    
    """%(agno, edadfutura)
    return HttpResponse(doc)


def odoo(request):
    
    url = 'http://localhost:8069'
    db = 'primera'
    username = 'usuario_api'
    password = '27475967'

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    model_name = 'res.partner'
    fields = ['name', 'email', 'phone']
    domain = []
    partners = models.execute_kw(db, uid, password, model_name, 'search_read', [domain], {'fields': fields})

    print(partners)
    
    return render(request, 'datos_api.html', {'fields': partners})