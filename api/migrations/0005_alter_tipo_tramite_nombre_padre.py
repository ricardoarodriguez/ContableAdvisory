# Generated by Django 4.1.6 on 2023-04-20 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_detalle_tramite_estado_tramite_tramite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_tramite',
            name='nombre_padre',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
