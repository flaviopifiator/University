# Generated by Django 2.1.2 on 2018-10-10 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universidad', '0001_initial'),
        ('util', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='universidad',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Departamento'),
        ),
        migrations.AddField(
            model_name='universidad',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Localidad'),
        ),
        migrations.AddField(
            model_name='universidad',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Pais'),
        ),
        migrations.AddField(
            model_name='universidad',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='util.Provincia'),
        ),
        migrations.AddField(
            model_name='aula',
            name='universidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universidad.Universidad'),
        ),
        migrations.AlterUniqueTogether(
            name='universidad',
            unique_together={('nombre', 'sigla')},
        ),
    ]
