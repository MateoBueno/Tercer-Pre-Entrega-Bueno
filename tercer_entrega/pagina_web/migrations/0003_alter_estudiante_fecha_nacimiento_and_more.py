# Generated by Django 4.1.4 on 2023-01-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0002_alter_estudiante_email_alter_profesor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
