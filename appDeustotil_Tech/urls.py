from django.urls import path
from . import views
from appDeustotil_Tech.views import EmpleadoDetailView

urlpatterns = [
    # ej: /miApp/
    path('', views.index, name='index'),
    path('/', views.index_proyectos, name='Proyectos'),
    path('/empleado/<int:pk>', EmpleadoDetailView.as_view(), name='empleado-show')
]
