from django.urls import path
from . import views
from appDeustotil_Tech.views import EmpleadoDetailView, EmpleadoListView
from appDeustotil_Tech.views import ProyectoDetailView
from appDeustotil_Tech.views import TareaListView

urlpatterns = [
    # ej: /miApp/
    path('', views.index, name='index'),
    path('/', views.index_proyectos, name='Proyectos'),
    path('/empleado/<int:pk>', EmpleadoDetailView.as_view(), name="empleado-show"),
    path('/empleado', EmpleadoListView.as_view() , name = "empleado-list"),
    path('/proyecto/<int:pk>', ProyectoDetailView.as_view(), name = "proyecto-show"),
    path('/tarea', TareaListView.as_view(), name = "tarea-list")
]
