# Generated by Django 5.0.4 on 2024-05-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustotil_Tech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='imagen',
            field=models.CharField(default=False, max_length=150),
        ),
    ]
