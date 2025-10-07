#books/urls.py
from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    # Libro
    path('libros/', views.LibroList.as_view(), name='libro-list'),
    path('libros/create/', views.LibroCreate.as_view(), name='libro-create'),
    path('libros/<int:pk>/', views.LibroDetail.as_view(), name='libro-detail'),
    path('libros/<int:pk>/update/', views.LibroUpdate.as_view(), name='libro-update'),
    path('libros/<int:pk>/delete/', views.LibroDelete.as_view(), name='libro-delete'),
    # Prestamo
    path('prestamos/', views.PrestamoList.as_view(), name='prestamo-list'),
    path('prestamos/create/', views.PrestamoCreate.as_view(), name='prestamo-create'),
    path('prestamos/<int:pk>/', views.PrestamoDetail.as_view(), name='prestamo-detail'),
    path('prestamos/<int:pk>/update/', views.PrestamoUpdate.as_view(), name='prestamo-update'),
    path('prestamos/<int:pk>/delete/', views.PrestamoDelete.as_view(), name='prestamo-delete'),

    path('', RedirectView.as_view(url='libros/')),
]