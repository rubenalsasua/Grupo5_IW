# Generated by Django 5.0.3 on 2024-05-28 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('appDeustotil_Tech', '0007_alter_empleado_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]