# Generated by Django 2.1.5 on 2019-03-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0047_auto_20190315_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='numero_albo',
            field=models.CharField(max_length=12, null=True, verbose_name="Numero di Iscrizione all'albo"),
        ),
    ]
