# Generated by Django 4.1.5 on 2023-10-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuari', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Usuario')),
                ('nombreUsuario', models.IntegerField(max_length=50, verbose_name='Nombre de usuario')),
                ('Contraseña', models.CharField(max_length=50, verbose_name='Contraseña de usuario')),
                ('Categoria', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('Email', models.CharField(max_length=50, verbose_name='Email de usuario')),
            ],
        ),
    ]