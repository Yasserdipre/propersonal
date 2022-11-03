from django.contrib import admin
from .models import Curso, Docente

# Register your models here.

@admin.register(Curso)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos')
    ordering = ('id',)
    list_display_links = ('nombre',)

admin.site.register(Docente)
