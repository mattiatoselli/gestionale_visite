# Generated by Django 2.1.5 on 2019-03-09 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0034_auto_20190309_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='stazione',
            field=models.ForeignKey(limit_choices_to={'status': 'Disponibile'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pianificazione_visite.stazione'),
        ),
    ]
