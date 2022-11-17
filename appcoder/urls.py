from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("estudiantes/", estudiantes, name="coder-estudiantes"),
    path("estudiantes/crear/", creacion_estudiantes, name="coder-estudiantes-crear"),
    path("estudiantes/buscar/", buscar_alumnos, name="coder-estudiantes-buscar"),
    path("profesores/", profesores, name="coder-profesores"),
    path("profesores/crear/", creacion_profesores, name="coder-profesores-crear"),
    path("cursos/", cursos, name="coder-cursos"),
    path("cursos/borrar/<id>", eliminar_curso, name="coder-cursos-borrar"),
    path("cursos/crear/", creacion_curso, name="coder-cursos-crear"),
    path("cursos/actualizar/<id>/", editar_curso, name="coder-cursos-editar"),

    path("cursos/buscar/", buscar_curso, name="coder-cursos-buscar"),
    path("cursos/buscar/resultados/", buscar_curso, name="coder-cursos-buscar-resultados"),
    path("entregables/detalle/", EntregablesDetail.as_view(), name="coder-entregables-details"),
    path("entregables/borrar/<pk>", EntregablesDeleteView.as_view(), name="coder-entregables-delete"),
    path("entregables/crear/", EntregablesCreateView.as_view(), name="coder-entregables-create"),
    path("entregables/actualizar/<pk>", EntregablesUpdateView.as_view(), name="coder-entregables-update"),
    path("entregables/", EntregablesList.as_view(), name="coder-entregables"),
]   

