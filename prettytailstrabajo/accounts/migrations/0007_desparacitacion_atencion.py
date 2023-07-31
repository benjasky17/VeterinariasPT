# Generated by Django 4.1.2 on 2023-07-03 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_vacunacion_documento_alter_vacunacion_nombre_vacuna_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desparacitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_desparacitacion', models.CharField(max_length=100)),
                ('tipo_desparacitacion', models.CharField(max_length=100)),
                ('documento', models.FileField(null=True, upload_to='infomascotas/')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_atencion', models.CharField(max_length=100)),
                ('tipo_atencion', models.CharField(max_length=100)),
                ('documento', models.FileField(null=True, upload_to='infomascotas/')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.mascota')),
            ],
        ),
    ]