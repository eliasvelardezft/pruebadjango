# Generated by Django 3.0 on 2021-04-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(max_length=50, verbose_name='DNI'),
        ),
    ]
