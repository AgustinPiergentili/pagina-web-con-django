# Generated by Django 4.1.3 on 2022-11-13 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Nombre_Usuario',
            new_name='Usuario',
        ),
    ]