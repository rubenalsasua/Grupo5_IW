from django.urls import path
from . import views
from appDeustotil_Tech.views import (
    EmpleadoDetailView,
    EmpleadoListView,
    EmpleadoCreateView, ProyectoCreateView, TareaCreateView, UsuarioDetailView, ClienteCreateView, ProyectoUpdateView,
    EmpleadoUpdateView, TareaUpdateView, ProyectoDeleteView, EmpleadoDeleteView, TareaDeleteView
)
from appDeustotil_Tech.views import ProyectoDetailView, ProyectoListView
from appDeustotil_Tech.views import TareaListView, TareaDetailView
from appDeustotil_Tech.views import mandar_email

urlpatterns = [

    path("/", views.login, name="login"),
    path('/login/buscar', views.buscar_usuario, name='buscar_usuario'),
    path("/login", UsuarioDetailView.as_view(), name="usuario-detail"),
    path("/index", views.index, name="index"),
    path("/proyectos", ProyectoListView.as_view(), name="proyecto-list"),
    path("/empleado/<int:pk>", EmpleadoDetailView.as_view(), name="empleado-show"),
    path('/empleado/buscar', views.buscar_empleado, name='buscar_empleado'),
    path("/empleados", EmpleadoListView.as_view(), name="empleado-list"),
    path("/empleado/create", EmpleadoCreateView.as_view(), name="empleado-create"),
    path("/proyecto/create", ProyectoCreateView.as_view(), name="proyecto-create"),
    path("/tarea/create", TareaCreateView.as_view(), name="tarea-create"),
    path("/proyecto/<int:pk>", ProyectoDetailView.as_view(), name="proyecto-show"),
    path('/proyecto/buscar', views.buscar_proyecto, name='buscar_proyecto'),
    path("/tareas", TareaListView.as_view(), name="tarea-list"),
    path("/tarea/<int:pk>", TareaDetailView.as_view(), name="tarea-show"),
    path("/proyectos/mandaremail", mandar_email, name="email-informe-proyectos"),
    path("/crearcliente", ClienteCreateView.as_view(), name="cliente-create"),
    path("/proyecto/<int:pk>/update", ProyectoUpdateView.as_view(), name="proyecto-update"),
    path("/empleado/<int:pk>/update", EmpleadoUpdateView.as_view(), name="empleado-update"),
    path("/tarea/<int:pk>/update", TareaUpdateView.as_view(), name="tarea-update"),
    path("/proyecto/<int:pk>/delete", ProyectoDeleteView.as_view(), name="proyecto-delete"),
    path("/empleado/<int:pk>/delete", EmpleadoDeleteView.as_view(), name="empleado-delete"),
    path("/tarea/<int:pk>/delete", TareaDeleteView.as_view(), name="tarea-delete"),
]
