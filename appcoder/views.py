from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import Curso  #Importamos la clase q vamos a trabar en este form
from appcoder.models import Profesor
from appcoder.forms import ProfesorFormulario
# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    #obtenemos el listado de objetos en la base de datos
    # curso = Curso.objects.all()

    # for curso in Curso:
    #     print(curso.nombre)

    return render(request, "appcoder/cursos.html")


def creacion_curso(request):
    #print(request.GET)
    #print(request.POST)
    #print(request.method)

    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]

        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()



    return render(request, "appcoder/curso_formulario.html")


    
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")




def creacion_profesores(request):

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            #recuperamos los datos
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"],apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save()

        return

    else:
        formulario = ProfesorFormulario()
    
    contexto = {"formulario": formulario}
    return render(request, "appcoder/profesores_formularios.html", contexto)

def buscar_curso(request):

    return render(request, "appcoder/busqueda_cursos.html")
    pass

def resultado_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]
    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)

    return render(request, "appcoder/resultado_busqueda_cursos.html", {"cursos":cursos})
    pass

def entregables(request):
    return render(request, "appcoder/entregables.html")

#def listado_cursos(request):
#    cursos = Curso.objects.all()

#    cadena_respuesta = ""
 #   for curso in cursos:
  #      cadena_respuesta += curso.nombre + " | "

   # return HttpResponse(cadena_respuesta)
