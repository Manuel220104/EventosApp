# Generated by Django 5.0.3 on 2024-03-05 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invitados', '0003_alter_invitados_mesa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitados',
            old_name='id',
            new_name='idInvitados',
        ),
    ]
