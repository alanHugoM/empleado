# Generated by Django 5.1.4 on 2025-01-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=20, verbose_name='Nombre_Corto')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
        ),
    ]
