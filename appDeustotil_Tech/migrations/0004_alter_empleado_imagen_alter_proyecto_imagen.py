# Generated by Django 5.0.4 on 2024-05-01 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appDeustotil_Tech", "0003_proyecto_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empleado",
            name="imagen",
            field=models.CharField(default=False, max_length=300),
        ),
        migrations.AlterField(
            model_name="proyecto",
            name="imagen",
            field=models.CharField(default=False, max_length=300),
        ),
    ]
