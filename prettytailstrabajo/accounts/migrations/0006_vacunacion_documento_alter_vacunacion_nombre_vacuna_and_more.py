# Generated by Django 4.1.2 on 2023-07-02 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_vacunacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacunacion',
            name='documento',
            field=models.FileField(null=True, upload_to='infomascotas/'),
        ),
        migrations.AlterField(
            model_name='vacunacion',
            name='nombre_vacuna',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vacunacion',
            name='tipo_vacuna',
            field=models.CharField(max_length=100),
        ),
    ]
