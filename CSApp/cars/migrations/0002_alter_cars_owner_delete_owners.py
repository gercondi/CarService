# Generated by Django 4.1.7 on 2023-02-24 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='owners.owners'),
        ),
        migrations.DeleteModel(
            name='Owners',
        ),
    ]