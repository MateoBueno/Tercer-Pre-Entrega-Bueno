from django.shortcuts import render,redirect
from django.urls import reverse 
from django.http import HttpResponse
from pagina_web.models import Estudiante,Profesor,Curso
from pagina_web.forms import CursoFormulario,EstudianteFormulario,ProfesorFormulario
from django.db.models import Q




def Inicio(request):
    return render(
        request= request, 
        template_name= 'pagina_web/inicio.html',
        )

def listar_estudiantes(request):
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request = request, 
        template_name= 'pagina_web/lista_estudiantes.html',
        context = contexto,
        )

def crear_estudiantes(request):
    formulario = EstudianteFormulario()
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiantes = Estudiante(nombre=data['nombre'], apellido=data['apellido'])
            estudiantes.save()
            url_exitosa = reverse('listar_estudiantes')
            return redirect(url_exitosa)
    #else:  # GET
       #formulario = EstudianteFormulario()
    return render(
        request=request,
        template_name='pagina_web/formulario_estudiante.html',
        context={'formulario': formulario},
    )


def buscar_estudiantes(request):
    if request.method == "POST":
        data = request.POST
        estudiantes = Estudiante.objects.filter(nombre__contains=data['nombre'])
        contexto = {
            'estudiantes' : estudiantes 
        }   
        return render(
            request = request,
            template_name='pagina_web/lista_estudiantes.html',
            context=contexto,
        )


#Profesores

def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request = request, 
        template_name = 'pagina_web/lista_profesores.html',
        context = contexto,
        )


def crear_profesores(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], materia=data['materia'])
            profesor.save()
            url_exitosa = reverse('listar_profesores')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    return render(
        request=request,
        template_name='pagina_web/formulario_profesores.html',
        context={'formulario': formulario},
    )

def buscar_profesores(request):
    if request.method == "POST":
        data = request.POST
        profesor = Profesor.objects.filter(nombre__contains=data['nombre'])
        contexto = {
            'profesores' : profesor
        }   
        return render(
            request = request,
            template_name='pagina_web/lista_profesores.html',
            context=contexto,
            )

#Cursos

def listar_cursos(request):
    contexto = {
        'curso': Curso.objects.all()
    }
    return render(
        request = request, 
        template_name = 'pagina_web/lista_cursos.html',
        context = contexto
        )

def crear_cursos(request):
    formulario = CursoFormulario()
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        #print(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            print(data)
            curso = Curso(nombre=data['nombre'], comision=data['comision'])
            curso.save()
        else:
            print("No es valido")
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
   
    return render(
        request=request,
        template_name='pagina_web/formulario_curso.html',
        context={'formulario': formulario},
    )
    
def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(nombre__contains=data['nombre'])
        contexto = {
            'curso' : cursos 
        }   
        return render(
            request = request,
            template_name='pagina_web/lista_cursos.html',
            context=contexto,
        )
    