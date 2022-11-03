from http.client import HTTPResponse
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Curso, Docente
from django.views.generic import ListView
from Aplicaciones.Academica.models import Docente

# Create your views here.


def home(request):
    Cursoslist = Curso.objects.all()
    data = {
        'titulo': 'Gestión de Cursos',
        'cursos': Cursoslist
    }
    return render(request,"index.html", data )



class CursoLV(ListView):
    model = Curso
    template_name = 'index.html'

    #Aquí filtramos la data a salir
    def get_queryset(self):
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Cursos'
        return context

def eliminarCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/')
        
def login(request):
    return render(request, 'login.html')

def error(request):
    return render(request, 'error.html')

def errorin(request):
    return render(request, 'errorin.html')

def inicio(request):
    data = {
      'nombre': request.GET.get('nombre'),
      
  }
    return render(request, 'inicio.html', data)

def registrarDatos(request):
    nombre = request.POST['txtNombre']
    apellidos = request.POST['txtApellidos']
    email = request.POST['email']
    contraseña = request.POST['contraseña']
    fechaNacimiento = request.POST['fecha']
    sexo = request.POST['genero']
    try1= Docente.objects.filter(email= email)
    if not try1:
        print('No hay nada')
        docentes = Docente.objects.create(nombre=nombre, apellidos= apellidos, email= email, contraseña= contraseña, fechaNacimiento= fechaNacimiento,sexo= sexo)
        return redirect('http://127.0.0.1:8000/login/')
    else:
        print('Si hay')
        return redirect('http://127.0.0.1:8000/error/')

def inisesion(request):
    email = request.POST['emailpri']
    contraseña = request.POST['contraseñapri']
    nombre= Docente.objects.filter(email= email, contraseña=contraseña)

    if not nombre:
        print('No hay nada')
        return redirect('http://127.0.0.1:8000/errorin/')
        
    else:
        dato= Docente.objects.get(email = email)
        print('Si hay, nombre es:', dato)
    return redirect('http://127.0.0.1:8000/inicio/?nombre=' + str(dato))
    