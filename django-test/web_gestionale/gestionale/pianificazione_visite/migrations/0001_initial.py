# Generated by Django 2.1.5 on 2019-02-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(help_text='Nome del medico.', max_length=50)),
                ('Last_Name', models.CharField(help_text='Cognome del medico', max_length=50)),
                ('Email', models.EmailField(max_length=90)),
            ],
        ),
    ]
