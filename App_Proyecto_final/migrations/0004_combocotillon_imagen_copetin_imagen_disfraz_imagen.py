# Generated by Django 4.0.6 on 2022-08-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Proyecto_final', '0003_golosinas_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='combocotillon',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='golosinass'),
        ),
        migrations.AddField(
            model_name='copetin',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='golosinass'),
        ),
        migrations.AddField(
            model_name='disfraz',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='golosinass'),
        ),
    ]
