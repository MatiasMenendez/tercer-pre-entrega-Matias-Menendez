from django.shortcuts import render
from django.http import HttpResponse
from AppPortfolio.models import Cursos, Tecnologias, Proyectos
from AppPortfolio.form import CursoFormulario2, ProyectoFormulario, TecnologiasFormulario


def inicio(req):
    return render(req, "../templates/appportfolio/padre.html")

def proyectos(req):
    return render(req, "../templates/appportfolio/proyectoFormulario.html")


def tecnologias(req):
    return render(req, "../templates/appportfolio/tecnologias.html")

def cursoFormulario(req):
        if req.method == 'POST':
            
            curso = Cursos(nombre=req.POST['curso'], camada=req.POST['camada'])
            
            curso.save()
            
            return render(req, "../templates/appportfolio/padre.html")
        
        return render(req, "../templates/appportfolio/cursoformulario.html")


def cursoFormulario2(req):
    
    if req.method == "POST":
        
        miFormulario = CursoFormulario2(req.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Cursos(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(req, "../templates/appportfolio/padre.html")
    else:
     miFormulario = CursoFormulario2()
            
    return render(req, "../templates/appportfolio/cursoformulario2.html", {"miFormulario": miFormulario})


def proyectoFormulario(req):
    
    if req.method == "POST":
        
        miForm = ProyectoFormulario(req.POST)
        print(miForm)
        
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            proyecto = Proyectos(nombre=informacion['nombre'], empresa=informacion['empresa'], email=informacion['email'])
            proyecto.save()
            return render(req, "../templates/appportfolio/padre.html")
    else:
     miForm = ProyectoFormulario()
            
    return render(req, "../templates/appportfolio/proyectoformulario.html", {"miForm": miForm})



def tecnologiasFormulario(req):
    
    if req.method == "POST":
        
        tecForm = TecnologiasFormulario(req.POST)
        print(tecForm)
        
        if tecForm.is_valid:
            informacion = tecForm.cleaned_data
            tecnologias = Tecnologias(nombre=informacion['nombre'], dificultad=informacion['dificultad'])
            tecnologias.save()
            return render(req, "../templates/appportfolio/padre.html")
    else:
     tecForm = TecnologiasFormulario()
            
    return render(req, "../templates/appportfolio/tecnologiasformulario.html", {"tecForm": tecForm})


def busquedaCamada(req):
    return render(req, "../templates/appportfolio/busquedaCamada.html")

def buscar(req):
    if req.GET['camada']:
        
        camada = req.GET['camada']
        
        cursos = Cursos.objects.filter(camada__icontains=camada)
        
        return render(req, "../templates/appportfolio/resultadoBusqueda.html", {"curso": cursos, "camada": camada})
    else:
        
        respuesta = "no enviaste datos"
    return HttpResponse(respuesta)