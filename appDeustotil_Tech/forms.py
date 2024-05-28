from django import forms

from appDeustotil_Tech.models import Proyecto, Empleado, Tarea, Cliente


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'presupuesto',
                  'cliente', 'jefe_proyecto', 'imagen']


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['dni', 'nombre', 'apellido', 'email', 'telefono', 'imagen']


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'proyecto', 'fecha_inicio', 'fecha_fin', 'empleado',
                  'prioridad', 'estado', 'apuntes']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
