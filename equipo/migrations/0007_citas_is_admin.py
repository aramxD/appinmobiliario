# Generated by Django 3.2.3 on 2021-06-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0006_citas_creado'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
