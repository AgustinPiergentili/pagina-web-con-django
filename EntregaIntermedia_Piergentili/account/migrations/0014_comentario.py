# Generated by Django 4.1.3 on 2022-12-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_reseña_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('comentario', models.CharField(max_length=240)),
            ],
        ),
    ]
