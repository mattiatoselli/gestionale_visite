# Generated by Django 2.1.5 on 2019-03-04 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0015_auto_20190304_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pianificazione_visite.Doctor'),
        ),
    ]