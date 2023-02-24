# Generated by Django 4.1.7 on 2023-02-24 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicestoCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porfacturar', models.CharField(choices=[('S', 'Facturado'), ('N', 'No Facturado')], default='N', max_length=1)),
                ('placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.owners')),
                ('servicio', models.ManyToManyField(to='services.services')),
            ],
        ),
    ]
