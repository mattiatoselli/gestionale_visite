# Generated by Django 2.1.5 on 2019-02-25 20:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0010_auto_20190224_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('ora_di_inizio', models.TimeField()),
            ],
        ),
    ]