from django.urls import path
from pagina_web.views import (Inicio,listar_estudiantes,listar_profesores,
listar_cursos, crear_cursos, buscar_cursos,crear_estudiantes,buscar_estudiantes,
crear_profesores,buscar_profesores,)


urlpatterns = [
    path('Inicio/', Inicio, name="iniciar"),

    path("estudiantes/", listar_estudiantes, name="listar_estudiantes"),
    path("crear-estudiantes/", crear_estudiantes, name="crear_estudiantes"),
    path("buscar-estudiantes/", buscar_estudiantes, name="buscar_estudiantes"),

    path("profesores/", listar_profesores, name="listar_profesores"),
    path("crear-profesores/",crear_profesores, name="crear_profesores"),
    path("buscar-profesores", buscar_profesores, name="buscar_profesores"),

    path("cursos/", listar_cursos, name="listar_cursos"),
    path("crear-cursos/", crear_cursos , name="crear_cursos"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
   
]