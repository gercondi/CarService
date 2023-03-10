# Generated by Django 4.1.7 on 2023-02-23 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('documento', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Propietario',
                'verbose_name_plural': 'Propietarios',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('placa', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('modelo', models.CharField(max_length=5)),
                ('marca', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.owners')),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
            },
        ),
    ]
