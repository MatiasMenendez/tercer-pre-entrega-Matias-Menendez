from django import forms

class CursoFormulario2(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
class ProyectoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    empresa = forms.CharField(max_length=40)
    email = forms.EmailField()
    
class TecnologiasFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    dificultad = forms.CharField(max_length=40)