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
from appDeustotil_Tech.forms import EmpleadoForm, ProyectoForm, TareaForm
from appDeustotil_Tech.models import Proyecto
from appDeustotil_Tech.models import Empleado
from appDeustotil_Tech.models import Tarea
from appDeustotil_Tech.models import Usuario

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


def login(request):
    return render(request, "PaginaLogin.html")


def index(request):
    return render(request, "appDeustotil_Tech/index.html")


# PROYECTOS VIEWS


class ProyectoListView(ListView):
    model = Proyecto
    template_name = "appDeustotil_Tech/proyecto_list.html"
    context_object_name = "proyectos"


def mandar_email(request):
    subject = 'Informe de proyectos'
    proyectos = Proyecto.objects.all()
    context = {'proyecto': proyectos}
    html_message = render_to_string('appDeustotil_Tech/email.html', context)
    plain_message = strip_tags(html_message)
    from_email = 'grupo5iw.deusto@gmail.com'
    recipient_list = ['r.alsasua@opendeusto.es']

    email = EmailMessage(subject, plain_message, from_email, recipient_list)
    email.content_subtype = 'html'
    email.send()

    return HttpResponse('Correo con plantilla enviado exitosamente.')


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


# LOGIN VIEWS (obtener los registros de la BBDD)

def ValidarUser(request):
    user = Usuario.objects.all()
    print(user)
    context_object_name = "usuario"
    return render(request, 'PaginaLogin.html')


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "PaginaLogin.html"
    context_object_name = "usuario"


def BuscarUser(request, usuario):
    UserObject = Usuario.objects.filter(user__icontains=usuario)
    return render(request, 'appDeustotil_Tech/prbLogin.html', {'Usuario': usuario})


# CREATE VIEWS

class TareaCreateView(View):
    def get(self, request):
        formulario = TareaForm()
        context = {"formulario": formulario}
        return render(request, "appDeustotil_Tech/tarea_create.html", context)

    def post(self, request):
        formulario = TareaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        return render(
            request,
            "appDeustotil_Tech/tarea_create.html",
            {"formulario": formulario},
        )


class ProyectoCreateView(View):
    def get(self, request):
        formulario = ProyectoForm()
        context = {"formulario": formulario}
        return render(request, "appDeustotil_Tech/proyecto_create.html", context)

    def post(self, request):
        formulario = ProyectoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        return render(
            request,
            "appDeustotil_Tech/proyecto_create.html",
            {"formulario": formulario},
        )
