# Generated by Django 2.1.5 on 2019-03-16 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0048_doctor_numero_albo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='doctor',
            unique_together={('Name', 'Last_Name', 'numero_albo')},
        ),
    ]
