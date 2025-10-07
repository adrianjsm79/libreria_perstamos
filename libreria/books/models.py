from django.db import models
from django.urls import reverse

class Libro(models.Model):
    ESTADO_CHOICES = [
        ('Libre', 'Libre'),
        ('Prestado', 'Prestado'),
    ]
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    portada = models.ImageField(upload_to='portadas/')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Libre')  # ✅ sin coma
    resumen = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} — {self.autor}"

    def get_absolute_url(self):
        return reverse('libro-detail', kwargs={'pk': self.pk})

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    usuario = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.libro.titulo} → {self.usuario}"
