from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, DeleteView, UpdateView
from appDeustotil_Tech.models import Proyecto
from appDeustotil_Tech.models import Empleado
from appDeustotil_Tech.models import Tarea


# Create your views here.

#PROYECTOS VIEWS
def index(request):
    return HttpResponse("Esta es nuestra aplicación de Django!")


def index_proyectos(request, proyecto_id):
    proyectos = get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'appDeustotil_Tech/proyecto_list.html', {'proyectos': proyectos})

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name  = 'appDeustotil_Tech/proyecto_detail.html'
    context_object_name = 'proyecto'



#EMPLEADOS VIEWS
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'appDeustotil_Tech/empleado_detail.html'
    context_object_name = 'empleado'

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'appDeustotil_Tech/empleado_list.html'
    context_object_name = 'empleado'


#TAREA VIEWS

class TareaListView(ListView):
    model = Tarea
    template_name = 'appDeustotil_Tech/tarea_list.html'
    context_object_name = 'tarea'




