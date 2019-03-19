# Generated by Django 2.1.5 on 2019-02-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Email_secondaria',
            field=models.EmailField(help_text='inserire un eventuale seconda Email.', max_length=90, null=True, verbose_name='Email Secondaria'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Numero_Telefonico',
            field=models.CharField(help_text='numero telefonico del medico', max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Numero_Telefonico_Secondario',
            field=models.CharField(help_text='Eventuale numero telefonico secondario', max_length=11, null=True, verbose_name='Numero telefonico secondario'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Email',
            field=models.EmailField(help_text='inserire un indirizzo mail valido.', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Last_Name',
            field=models.CharField(help_text="Cognome del medico. Inserire con l'iniziale maisucola e le restanti lettere minuscole.", max_length=50, null=True, verbose_name='Cognome'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Name',
            field=models.CharField(help_text="Nome del medico. Inserire con l'iniziale maisucola e le restanti lettere minuscole.", max_length=50, null=True, verbose_name='Nome'),
        ),
    ]
