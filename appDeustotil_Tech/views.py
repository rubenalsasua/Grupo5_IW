from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    View,
    DeleteView,
    UpdateView,
    CreateView,
)
from appDeustotil_Tech.forms import EmpleadoForm
from appDeustotil_Tech.models import Proyecto
from appDeustotil_Tech.models import Empleado
from appDeustotil_Tech.models import Tarea


# Create your views here.


def index(request):
    return HttpResponse("Esta es nuestra aplicación de Django!")


# PROYECTOS VIEWS


class ProyectoListView(ListView):
    model = Proyecto
    template_name = "appDeustotil_Tech/proyecto_list.html"
    context_object_name = "proyectos"


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = "appDeustotil_Tech/proyecto_detail.html"
    context_object_name = "proyecto"


# EMPLEADOS VIEWS
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "appDeustotil_Tech/empleado_detail.html"
    context_object_name = "empleado"


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appDeustotil_Tech/empleado_list.html"
    context_object_name = "empleado"


class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        context = {"formulario": formulario}
        return render(request, "appDeustotil_Tech/empleado_create.html", context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        return render(
            request,
            "appDeustotil_Tech/empleado_create.html",
            {"formulario": formulario},
        )


# TAREA VIEWS


class TareaListView(ListView):
    model = Tarea
    template_name = "appDeustotil_Tech/tarea_list.html"
    context_object_name = "tarea"


class TareaDetailView(DetailView):
    model = Tarea
    template_name = "appDeustotil_Tech/tarea_detail.html"
    context_object_name = "tarea"
