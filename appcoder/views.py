from django.http import HttpResponse
from django.shortcuts import render, redirect
from appcoder.models import Curso  #Importamos la clase q vamos a trabar en este form
from appcoder.models import Profesor, Estudiante, Entregable
from appcoder.forms import ProfesorFormulario, EstudianteFormulario, CursoFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):

    errores= ""
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data =formulario.cleaned_data
            curso = Curso(nombre=data["nombre"], camada=data["camada"])
            curso.save()
        else:

            errores = formulario.errors


    cursos =Curso.objects.all() #obtener todo los registros del modelo
    formulario = CursoFormulario
    contexto = {"listado_cursos": cursos, "formulario": formulario, "errores": errores}

    return render(request, "appcoder/cursos.html",contexto)

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre = data["nombre"]
            curso.camada = data["camada"]
            curso.save()
            return redirect("coder-cursos")
        else:
            return render(request, "appcoder/editar_curso.html", {"formulario": formulario, "errores": formulario.errors})    

    else:
        formulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})
        return render(request, "appcoder/editar_curso.html", {"formulario": formulario, "errores": ""})



def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect("coder-cursos")





def creacion_curso(request):
    print(request.GET)
    print(request.POST)
    print(request.method)


    if request.method == "POST": #verificamos q sea post la validacion
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]

        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()

    return render(request, "appcoder/curso_formulario.html")



    
    
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def creacion_estudiantes(request):

    if request.method== "POST":
        formulario = EstudianteFormulario(request.POST)
        if formulario.is_valid(): #valida y carga los datos en el cleaned data, por eso tiene que estar si o si
            #accedemos al dic q contien la info del formulario
            data = formulario.cleaned_data

            estudiante = Estudiante(nombre=data["nombre"], apellido=data["apellido"],email=data["email"])
            estudiante.save()

    formulario = EstudianteFormulario()
    return render(request, "appcoder/estudiantes_formulario.html",{"formulario":formulario})
    

def profesores(request):
    return render(request, "appcoder/profesores.html")




def creacion_profesores(request):

     if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])

            profesor.save()

        formulario = ProfesorFormulario()  
    
        contexto = {"formulario": formulario}
        return render(request, "appcoder/profesores_formularios.html", contexto)

def buscar_curso(request):

    return render(request, "appcoder/busqueda_cursos.html")
    pass

def resultado_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]
    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)

    return render(request, "appcoder/resultado_busqueda_cursos.html", {"listado_alumnos":estudiantes})



def buscar_alumnos(request):

    if request.GET:
        estudiantes = Estudiante.objects.filter(nombre__icontains=request.get["nombre_alumno"])
        return render(request, "appcoder/busqueda_estudiantes.html", {"cursos":[]})


    return render(request,)

def entregables(request):
    return render(request, "appcoder/entregables.html")

#def listado_cursos(request):
#    cursos = Curso.objects.all()

#    cadena_respuesta = ""
 #   for curso in cursos:
  #      cadena_respuesta += curso.nombre + " | "

   # return HttpResponse(cadena_respuesta)

class EntregablesList(ListView):

    model = Entregable
    template_name = "coder/entregables/"

class EntregablesDetail(DetailView):

    model = Entregable
    template_name = "appcoder/detail_entregables"

class EntregablesCreateView(CreateView):

    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["nombre","fecha_de_entrega", "entregado"]

class EntregablesUpdateView(UpdateView):

    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["nombre","fecha_de_entrega", "entregado"]

class EntregablesDeleteView(DeleteView):
    model = Entregable
    success_url = "coder/entregables/"