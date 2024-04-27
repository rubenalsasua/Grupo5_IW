from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, DeleteView, UpdateView


from appDeustotil_Tech.models import Proyecto


# Create your views here.
def index(request):
    return HttpResponse("Esta es nuestra aplicación de Django!")


def index_proyectos(request, proyecto_id):
    proyectos = get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'appDeustotil_Tech/proyecto_list.html', {'proyectos': proyectos})
