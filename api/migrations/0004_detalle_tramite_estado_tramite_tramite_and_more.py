# Generated by Django 4.1.6 on 2023-04-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_blog_contable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tramite', models.IntegerField(null=True)),
                ('observaciones', models.CharField(max_length=2000, null=True)),
                ('id_servicio', models.IntegerField(null=True)),
                ('created_by', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attached_file_path', models.CharField(max_length=150, null=True)),
                ('id_estado', models.IntegerField(null=True)),
                ('estado', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('created_by', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tipo_tramite', models.IntegerField(null=True)),
                ('tipo_tramite', models.CharField(max_length=100, null=True)),
                ('id_proceso', models.IntegerField(null=True)),
                ('proceso', models.CharField(max_length=100, null=True)),
                ('attached_file_path', models.CharField(max_length=150, null=True)),
                ('created_by', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_estado', models.IntegerField(null=True)),
                ('estado', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Detalle_Servicio',
        ),
        migrations.DeleteModel(
            name='Estado_Servicio',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.RenameField(
            model_name='tipo_tramite',
            old_name='descripcion_tipo',
            new_name='tipo_tramite',
        ),
        migrations.RemoveField(
            model_name='tipo_tramite',
            name='nombre_tipo',
        ),
        migrations.AddField(
            model_name='tipo_tramite',
            name='created_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tipo_tramite',
            name='id_padre',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tipo_tramite',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tipo_tramite',
            name='is_process',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tipo_tramite',
            name='nombre_padre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]