# Generated by Django 2.1.2 on 2018-10-10 10:20

from django.db import migrations, models
import django.db.models.deletion
import django_autoslugfield.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facultad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioMateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.TimeField(blank=True, null=True)),
                ('fin', models.TimeField(blank=True, null=True)),
                ('dias', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sábado'), ('Domingo', 'Domingo')], max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Horario Materia',
                'verbose_name_plural': 'Horarios de Materia',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', django_autoslugfield.fields.AutoSlugField(blank=True, max_length=255, null=True, title_field=None, unique=True)),
                ('año', models.CharField(blank=True, choices=[('1', '1°'), ('2', '2°'), ('3', '3°'), ('4', '4°'), ('5', '5°'), ('6', '6°'), ('7', '7°')], max_length=1, null=True)),
                ('periodo', models.CharField(blank=True, choices=[('AN', 'Anual'), ('1C', 'Primer Cuatrimetre'), ('2C', 'Segundo Cuatrimestre')], max_length=2, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('sigla', models.CharField(blank=True, max_length=50, null=True)),
                ('correlativas_aprobar', models.ManyToManyField(blank=True, related_name='_materia_correlativas_aprobar_+', to='materia.Materia')),
                ('correlativas_cursar', models.ManyToManyField(blank=True, related_name='_materia_correlativas_cursar_+', to='materia.Materia')),
                ('planes_estudio', models.ManyToManyField(to='facultad.PlanEstudio')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='ModoProfesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modo', models.CharField(choices=[('TE', 'Teórico'), ('PR', 'Práctico')], max_length=2)),
                ('horario_materia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='modo_profesores', to='materia.HorarioMateria')),
                ('profesores', models.ManyToManyField(to='facultad.Profesor')),
            ],
            options={
                'verbose_name': 'Materia Profesor',
                'verbose_name_plural': 'Materias Profesores',
            },
        ),
    ]