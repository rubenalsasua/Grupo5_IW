from django.urls import path
from . import views

urlpatterns = [
    # ej: /miApp/
    path('', views.index, name='index'),
    path('/', views.index_proyectos, name='Proyectos')
]
