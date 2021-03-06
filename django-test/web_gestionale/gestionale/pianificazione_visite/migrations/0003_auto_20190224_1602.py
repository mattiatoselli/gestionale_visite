# Generated by Django 2.1.5 on 2019-02-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0002_auto_20190224_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Email_secondaria',
            field=models.EmailField(blank=True, help_text='inserire un eventuale seconda Email.', max_length=90, null=True, verbose_name='Email Secondaria'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Numero_Telefonico_Secondario',
            field=models.CharField(blank=True, help_text='Eventuale numero telefonico secondario', max_length=11, null=True, verbose_name='Numero telefonico secondario'),
        ),
    ]
