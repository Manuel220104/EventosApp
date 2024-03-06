# Generated by Django 5.0.3 on 2024-03-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regalos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regalos',
            name='EnlaceRegalo',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Enlace del Regalo'),
        ),
        migrations.AlterField(
            model_name='regalos',
            name='ImagenUrl',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Url Imagen del Regalo'),
        ),
    ]