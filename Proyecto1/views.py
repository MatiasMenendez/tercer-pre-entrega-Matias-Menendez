from django.http import HttpResponse
from django.template import Template, Context, loader
from AppPortfolio.models import Cursos

def saludo(request):
    return HttpResponse("Holas Django - coder")

def probando_template(request):
    
    nom = "Mati"
    
    ap = "Pardo"
    
    diccionario = {"nombre": nom, "apellido":ap}
    
    plantilla = loader.get_template('template.html')
   
    documento = plantilla.render(diccionario)

    
    return HttpResponse(documento)
    
    
def agregar_curso(request, nom, cam):
    curso = Cursos(nombre=nom, camada=cam)
    curso.save()
    
    return HttpResponse("Curso agregado")
