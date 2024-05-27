# Generated by Django 5.0.3 on 2024-05-26 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustotil_Tech', '0005_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['-created'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='datos_cliente',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='imagen',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appDeustotil_Tech.cliente'),
        ),
    ]