from django.shortcuts import render
from django.db import models
from appDeustotil_Tech.models import Usuario


def ValidarUser(request):
    user = Usuario.objects.all()
    return render(request, 'productos.html', {'Usuario': user})
