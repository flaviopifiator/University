# Generated by Django 2.1.2 on 2018-10-10 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universidad', '0001_initial'),
        ('util', '0001_initial'),
        ('facultad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultad',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Departamento'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Localidad'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Pais'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Provincia'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='universidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultades', to='universidad.Universidad'),
        ),
        migrations.AddField(
            model_name='departamentofacultad',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Departamento'),
        ),
        migrations.AddField(
            model_name='departamentofacultad',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='facultad.Facultad'),
        ),
        migrations.AddField(
            model_name='departamentofacultad',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Localidad'),
        ),
        migrations.AddField(
            model_name='departamentofacultad',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Pais'),
        ),
        migrations.AddField(
            model_name='departamentofacultad',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Provincia'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carreras', to='facultad.DepartamentoFacultad'),
        ),
        migrations.AlterUniqueTogether(
            name='planestudio',
            unique_together={('año', 'carrera')},
        ),
    ]