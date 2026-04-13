from django.contrib import admin
from .models import Registro

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'fecha', 'descripcion')