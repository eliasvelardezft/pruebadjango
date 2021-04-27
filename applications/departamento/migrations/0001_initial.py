# Generated by Django 3.0 on 2021-04-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=100, verbose_name='Nombre Corto')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
        ),
    ]