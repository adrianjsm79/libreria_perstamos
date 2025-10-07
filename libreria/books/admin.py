from django.contrib import admin
from .models import Libro, Prestamo

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','estado')
    search_fields = ('titulo','autor')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro','usuario','fecha_inicio','fecha_fin')
    list_filter = ('fecha_inicio',)
