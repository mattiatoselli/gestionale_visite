# Generated by Django 2.1.5 on 2019-03-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0051_auto_20190318_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
