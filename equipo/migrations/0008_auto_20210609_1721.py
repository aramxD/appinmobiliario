# Generated by Django 3.2.3 on 2021-06-10 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0007_citas_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citas',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='asesor',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
