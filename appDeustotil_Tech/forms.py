from django import forms

from appDeustotil_Tech.models import Proyecto,Empleado,Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'