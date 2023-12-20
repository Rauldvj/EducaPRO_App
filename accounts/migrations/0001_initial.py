# Generated by Django 4.2.6 on 2023-12-19 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('localidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='media/default.png', upload_to='users/', verbose_name='Imagen de perfil')),
                ('rut', models.CharField(max_length=15, verbose_name='Rut')),
                ('direccion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección')),
                ('telefono', models.CharField(blank=True, max_length=9, null=True, verbose_name='Teléfono')),
                ('creado_por_coordinador', models.BooleanField(blank=True, default=True, null=True, verbose_name='Creado por el Coordinador')),
                ('comuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localidad.comuna', verbose_name='Comuna')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localidad.region', verbose_name='Region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'ordering': ['-id'],
            },
        ),
    ]
