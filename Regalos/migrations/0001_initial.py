# Generated by Django 5.0.3 on 2024-03-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regalos',
            fields=[
                ('idInvitados', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('ImagenUrl', models.URLField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Regalos',
            },
        ),
    ]