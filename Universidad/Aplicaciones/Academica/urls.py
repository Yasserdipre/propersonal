from django.urls import path
from Aplicaciones.Academica.views import CursoLV, eliminarCurso, login, registrarDatos, error, inisesion, inicio, errorin



urlpatterns = [
    path('', CursoLV.as_view(), name='gestion_cursos'),
    path('eliminacionCurso/<int:id>', eliminarCurso),
    path('login/', login),
    path('registrarDatos/', registrarDatos),
    path('error/', error),
    path('errorin/', errorin),
    path('inisesion/', inisesion),
    path('inicio/', inicio)
]