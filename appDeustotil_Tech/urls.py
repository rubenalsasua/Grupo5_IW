from django.urls import path
from . import views
from appDeustotil_Tech.views import (
    EmpleadoDetailView,
    EmpleadoListView,
    EmpleadoCreateView, ProyectoCreateView, TareaCreateView, UsuarioDetailView
)
from appDeustotil_Tech.views import ProyectoDetailView, ProyectoListView
from appDeustotil_Tech.views import TareaListView, TareaDetailView
from appDeustotil_Tech.views import mandar_email

urlpatterns = [

    path("/", views.login, name="login"),
    path('/buscar/<str:user>/', views.BuscarUser, name='buscar-user'),
    path("/login", UsuarioDetailView.as_view(), name="usuario-detail"),
    path("/index", views.index, name="index"),
    path("/proyectos", ProyectoListView.as_view(), name="proyecto-list"),
    path("/empleado/<int:pk>", EmpleadoDetailView.as_view(), name="empleado-show"),
    path("/empleados", EmpleadoListView.as_view(), name="empleado-list"),
    path("/empleado/create", EmpleadoCreateView.as_view(), name="empleado-create"),
    path("/proyecto/create", ProyectoCreateView.as_view(), name="proyecto-create"),
    path("/tarea/create", TareaCreateView.as_view(), name="tarea-create"),
    path("/proyecto/<int:pk>", ProyectoDetailView.as_view(), name="proyecto-show"),
    path("/tareas", TareaListView.as_view(), name="tarea-list"),
    path("/tarea/<int:pk>", TareaDetailView.as_view(), name="tarea-show"),
    path("/proyectos/mandaremail", mandar_email, name="email-informe-proyectos"),
]
