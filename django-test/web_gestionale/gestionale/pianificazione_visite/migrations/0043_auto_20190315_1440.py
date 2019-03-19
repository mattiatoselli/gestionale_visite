# Generated by Django 2.1.5 on 2019-03-15 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0042_auto_20190315_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['Last_Name', 'Name'], 'permissions': (('can view HCT doctor', 'can view HCT doctor'), ('can view med+ doctor', 'can view med+ doctor'), ('can edit med+ doctor', 'can edit med+ doctor'), ('can edit HCT doctor', 'can edit HCT doctor'), ('can create HCT doctor', 'can create HCT doctor'), ('can create med+ doctor', 'can create med+ doctor')), 'verbose_name': 'Dottore', 'verbose_name_plural': 'Dottori'},
        ),
    ]