from AppPortfolio import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('tecnologiasFormulario/', views.tecnologiasFormulario, name='tecnologiasFormulario'),
    path('proyectosFormulario/', views.proyectoFormulario, name='proyectosFormulario'),
    path('cursoFormulario2/', views.cursoFormulario2, name='cursoFormulario2'),
    path('busquedaCamada/', views.busquedaCamada, name='busquedaCamada'),
    path('buscar/', views.buscar),
]