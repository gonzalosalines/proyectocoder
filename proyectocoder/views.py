
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola chicos :) ")

def dia_hoy(request):
    hoy = datetime.now()

    respuesta = (f"Hoy es {hoy}")
    return HttpResponse(respuesta)

def anio_nacimiento(request, edad):
    
    edad = int(edad)

    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {anio_nac}")

def vista_plantilla(request):
    #Abrimos el file
    archivo = open(r"G:\Gonzalo\Curso de Python CoderHouse\17_django\proyectocoder\proyectocoder\templates\plantilla_bonita.html")
    #creamos el onject plantilla
    plantilla = Template(archivo.read())
    #cerramos el file
    archivo.close

    #Diccionario con datos para la plantilla
    datos = {"nombre": "Leonel", "fecha": datetime.now(),"apellido": "Gareis", "edad": 24}
    #despues mira la plantilla con los dos puntos , le erre ahi seguro
    # creamos el contexto
    contexto = Context()
    #renderizamos la plantilla para crear repuesta
    documento = plantilla.render(contexto)
    #retornamos repuesta
    return HttpResponse(documento)

def vista_listado_alumnos(request):

    #Abrimos el file
    archivo = open(r"G:\Gonzalo\Curso de Python CoderHouse\17_django\proyectocoder\proyectocoder\templates\listado_alumnos.html")
     #creamos el object plantilla
    plantilla = Template(archivo.read())
    #cerramos el file
    archivo.close
    #Diccionario de datos
    listado_alumnos = ["Leonel", "Juan","Barbara"]
    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}

    # creamos el contexto // le pasamos los datos q queremos meter en la lista
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

#para hacerlo con un loader de manera mas rapiday sencilla
def vista_listado_alumnos2(request):

        #Diccionario de datos
        listado_alumnos = ["Leonel", "Juan","Barbara"]
        datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}


        plantilla = loader.get_template("listado_alumnos.html")
        documento = plantilla.render(datos)

        return HttpResponse(documento)       




    