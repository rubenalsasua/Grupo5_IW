from django.db import models


# Create your models here.


class Empleado(models.Model):
    dni = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField(max_length=100)
    imagen = models.CharField(max_length=300, default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["-created"]


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    datos_cliente = models.TextField(max_length=100)
    jefe_proyecto = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=300, default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.datos_cliente}"

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]


class Tarea(models.Model):
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["-created"]

    class Prioridad(models.TextChoices):
        ALTA = "Alta", "Alta"
        MEDIA = "Media", "Media"
        BAJA = "Baja", "Baja"

    class Estado(models.TextChoices):
        ABIERTA = "ABIERTA", "ABIERTA"
        ASIGNADA = "ASIGNADA", "ASIGNADA"
        EN_PROCESO = "EN PROCESO", "EN PROCESO"
        FINALIZADA = "FINALIZADA", "FINALIZADA"

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=100, choices=Prioridad.choices)
    estado = models.CharField(max_length=100, choices=Estado.choices)
    apuntes = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.estado}"



class Usuario(models.Model):
    user = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.password}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuario"
        ordering = ["-created"]