# Generated by Django 3.2.3 on 2021-06-17 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0006_inmueble_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='ubicacion',
            field=models.URLField(blank=True, null=True),
        ),
    ]
