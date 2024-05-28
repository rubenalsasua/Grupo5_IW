from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    View,
    DeleteView,
    UpdateView,
    CreateView,
)
from appDeustotil_Tech.forms import EmpleadoForm, ProyectoForm, TareaForm, ClienteForm
from appDeustotil_Tech.models import Proyecto, Cliente
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
    return render(request, "login.html")


def index(request):
    return render(request, "appDeustotil_Tech/index.html")


# PROYECTOS VIEWS


class ProyectoListView(ListView):
    model = Proyecto
    template_name = "appDeustotil_Tech/proyectos/proyecto_list.html"
    context_object_name = "proyectos"


def mandar_email(request):
    subject = 'Informe de proyectos'
    proyectos = Proyecto.objects.all()
    context = {'proyectos': proyectos}
    html_message = render_to_string('../templates/email.html', context)
    plain_message = strip_tags(html_message)
    from_email = 'grupo5iw.deusto@gmail.com'
    recipient_list = ['r.alsasua@opendeusto.es', 'manel.diaz@opendeusto.es', 'asiernava23@gmail.com']

    email = EmailMessage(subject, plain_message, from_email, recipient_list)
    email.content_subtype = 'html'
    email.send()

    return HttpResponse('El correo electrónico se ha mandado a ' + recipient_list[0] + recipient_list[1] +
                        recipient_list[2] + 'correctamente')


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = "appDeustotil_Tech/proyectos/proyecto_detail.html"
    context_object_name = "proyecto"


def buscar_proyecto(request):
    nombre = request.GET.get('nombre', '')
    Proyectos = []

    if nombre:
        Proyectos = Proyecto.objects.filter(nombre__icontains=nombre)

    return render(request, 'appDeustotil_Tech/proyectos/proyecto_buscar.html', {'proyectos': Proyectos})






# EMPLEADOS VIEWS
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "appDeustotil_Tech/empleados/empleado_detail.html"
    context_object_name = "empleado"


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appDeustotil_Tech/empleados/empleado_list.html"
    context_object_name = "empleado"

def buscar_empleado(request):
    nombre = request.GET.get('nombre', '')
    apellido = request.GET.get('apellido', '')
    empleados = []

    if nombre and apellido:
        empleados = Empleado.objects.filter(nombre__icontains=nombre, apellido__icontains=apellido)
    elif nombre:
        empleados = Empleado.objects.filter(nombre__icontains=nombre)
    elif apellido:
        empleados = Empleado.objects.filter(apellido__icontains=apellido)

    return render(request, 'appDeustotil_Tech/empleados/empleado_buscar.html', {'empleados': empleados})


class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        context = {"formulario": formulario}
        return render(request, "appDeustotil_Tech/empleados/empleado_create.html", context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        return render(
            request,
            "appDeustotil_Tech/empleados/empleado_create.html",
            {"formulario": formulario},
        )










# TAREA VIEWS


class TareaListView(ListView):
    model = Tarea
    template_name = "appDeustotil_Tech/tareas/tarea_list.html"
    context_object_name = "tarea"


class TareaDetailView(DetailView):
    model = Tarea
    template_name = "appDeustotil_Tech/tareas/tarea_detail.html"
    context_object_name = "tarea"


# LOGIN VIEWS (obtener los registros de la BBDD)

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "login.html"
    context_object_name = "usuario"

def buscar_usuario(request):
    user = request.GET.get('user', '')
    password = request.GET.get('password', '')
    Usuarios = []

    print(f"user: {user}, password: {password}")

    if user and password:
        # Utilizar una búsqueda exacta para ambos campos
        Usuarios = Usuario.objects.filter(user=user, password=password)
        if Usuarios.exists():
            return redirect("/appDeustotil_Tech/index")

    return redirect("/appDeustotil_Tech/")


# CREATE VIEWS

class TareaCreateView(View):
    def get(self, request):
        formulario = TareaForm()
        context = {"formulario": formulario}
        return render(request, "appDeustotil_Tech/tareas/tarea_create.html", context)

    def post(self, request):
        formulario = TareaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        return render(
            request,
            "appDeustotil_Tech/tareas/tarea_create.html",
            {"formulario": formulario},
        )


class ProyectoCreateView(View):
    def get(self, request):
        formulario = ProyectoForm()
        context = {"formulario": formulario}
        return render(request, "appDeustotil_Tech/proyectos/proyecto_create.html", context)

    def post(self, request):
        formulario = ProyectoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        return render(
            request,
            "appDeustotil_Tech/proyectos/proyecto_create.html",
            {"formulario": formulario},
        )


class ClienteCreateView(View):
    def get(self, request):
        formulario = ClienteForm()
        context = {"formulario": formulario}
        return render(request, "appDeustotil_Tech/clientes/cliente_create.html", context)

    def post(self, request):
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        return render(
            request,
            "appDeustotil_Tech/clientes/cliente_create.html",
            {"formulario": formulario},
        )


class ProyectoUpdateView(UpdateView):
    model = Proyecto

    def get(self, request, pk):
        proyecto = Proyecto.objects.get(id=pk)
        formulario = ProyectoForm(instance=proyecto)
        context = {
            'formulario': formulario,
            'proyecto': proyecto
        }
        return render(request, 'appDeustotil_Tech/proyectos/proyecto_update.html', context)

    def post(self, request, pk):
        proyecto = Proyecto.objects.get(id=pk)
        formulario = ProyectoForm(request.POST, instance=proyecto)
        if formulario.is_valid():
            formulario.save()
            return redirect('proyecto-show', proyecto.id)
        else:
            formulario = ProyectoForm(instance=proyecto)
        return render(request, 'appDeustotil_Tech/proyectos/proyecto_update.html', {'formulario': formulario})


class EmpleadoUpdateView(UpdateView):
    model = Empleado

    def get(self, request, pk):
        empleado = Empleado.objects.get(id=pk)
        formulario = EmpleadoForm(instance=empleado)
        context = {
            'formulario': formulario,
            'empleado': empleado
        }
        return render(request, 'appDeustotil_Tech/empleados/empleado_update.html', context)

    def post(self, request, pk):
        empleado = Empleado.objects.get(id=pk)
        formulario = EmpleadoForm(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleado-show', empleado.id)
        else:
            formulario = EmpleadoForm(instance=empleado)
        return render(request, 'appDeustotil_Tech/empleados/empleado_update.html', {'formulario': formulario})


class TareaUpdateView(UpdateView):
    model = Tarea

    def get(self, request, pk):
        tarea = Tarea.objects.get(id=pk)
        formulario = TareaForm(instance=tarea)
        context = {
            'formulario': formulario,
            'tarea': tarea
        }
        return render(request, 'appDeustotil_Tech/tareas/tarea_update.html', context)

    def post(self, request, pk):
        tarea = Tarea.objects.get(id=pk)
        formulario = TareaForm(request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarea-show', tarea.id)
        else:
            formulario = TareaForm(instance=tarea)
        return render(request, 'appDeustotil_Tech/tareas/tarea_update.html', {'formulario': formulario})

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('index')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('index')

class TareaDeleteView(DeleteView):
    model = Tarea
    success_url = reverse_lazy('index')
