from django import forms

from appDeustotil_Tech.models import Proyecto,Empleado,Tareas

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class TareasForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = '__all__'