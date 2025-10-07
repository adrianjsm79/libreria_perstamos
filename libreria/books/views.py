from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro, Prestamo

# LIBRO
class LibroList(ListView):
    model = Libro
    paginate_by = 10

class LibroDetail(DetailView):
    model = Libro

class LibroCreate(CreateView):
    model = Libro
    fields = ['titulo','autor','portada','estado','resumen']

class LibroUpdate(UpdateView):
    model = Libro
    fields = ['titulo','autor','portada','estado','resumen']

class LibroDelete(DeleteView):
    model = Libro
    success_url = reverse_lazy('libro-list')

# PRESTAMO
class PrestamoList(ListView):
    model = Prestamo
    paginate_by = 10

class PrestamoDetail(DetailView):
    model = Prestamo

class PrestamoCreate(CreateView):
    model = Prestamo
    fields = ['libro', 'usuario', 'fecha_inicio', 'fecha_fin', 'notas']
    success_url = reverse_lazy('prestamo-list')  

    def form_valid(self, form):
        resp = super().form_valid(form)
        libro = form.instance.libro
        libro.estado = 'PREST'
        libro.save()
        return resp

class PrestamoUpdate(UpdateView):
    model = Prestamo
    fields = ['libro','usuario','fecha_inicio','fecha_fin','notas']

class PrestamoDelete(DeleteView):
    model = Prestamo
    success_url = reverse_lazy('prestamo-list')

