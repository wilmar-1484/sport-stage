# Generated by Django 3.2.8 on 2021-12-07 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proSportStage', '0003_loginusuarios_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginusuarios',
            name='cedula',
            field=models.IntegerField(null='True', verbose_name='Cedula'),
        ),
    ]
