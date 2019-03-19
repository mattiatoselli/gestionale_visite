# Generated by Django 2.1.5 on 2019-02-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pianificazione_visite', '0007_auto_20190224_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Provincia',
            field=models.CharField(blank=True, choices=[('AG', 'AGRIGENTO'), ('AN', 'ANCONA'), ('AO', 'AOSTA'), ('AQ', "L'AQUILA"), ('AG', 'Agrigento'), ('AR', 'AREZZO'), ('AP', 'ASCOLI-PICENO'), ('AT', 'ASTI'), ('AV', 'AVELLINO'), ('BA', 'BARI'), ('BT', 'BARLETTA'), ('BL', 'BELLUNO'), ('BN', 'BENEVENTO'), ('BG', 'BERGAMO'), ('BI', 'BIELLA'), ('BO', 'BOLOGNA'), ('BZ', 'BOLZANO'), ('BS', 'BRESCIA'), ('BR', 'BRINDISI'), ('CA', 'CAGLIARI'), ('CL', 'CALTANISETTA'), ('CB', 'CAMPOBASSO'), ('CI', 'CARBONIA IGLESIAS'), ('CE', 'CASERTA'), ('CT', 'CATANIA'), ('CZ', 'CATANZARO'), ('CH', 'CHIETI'), ('CO', 'COMO'), ('CS', 'COSENZA'), ('CR', 'CREMONA'), ('KR', 'CROTONE'), ('CN', 'CUNEO'), ('EN', 'ENNA'), ('FM', 'FERMO'), ('FE', 'FERRARA'), ('FI', 'FIRENZE'), ('FG', 'FOGGIA'), ('FC', 'FORLI-CESENA'), ('FR', 'FROSINONE'), ('GE', 'GENOVA'), ('GO', 'GORIZIA'), ('GR', 'GROSSETO'), ('IM', 'IMPERIA'), ('IS', 'ISERNIA'), ('SP', 'LA SPEZIA'), ('LT', 'LATINA'), ('LE', 'LECCE'), ('LC', 'LECCO'), ('LI', 'LIVORNO'), ('LO', 'LODI'), ('LU', 'LUCCA'), ('MC', 'MACERATA'), ('MN', 'MANTOVA'), ('MS', 'MASSA CARRARA'), ('MT', 'MATERA'), ('MI', 'MILANO'), ('MO', 'MODENA'), ('MB', 'MONZA BRIANZA'), ('NA', 'NAPOLI'), ('NO', 'NOVARA'), ('NU', 'NUORO'), ('OG', 'OGLIASTRA'), ('OT', 'OLBIA TEMPIO'), ('OR', 'ORISTANO'), ('PD', 'PADOVA'), ('PA', 'PALERMO'), ('PR', 'PARMA'), ('PV', 'PAVIA'), ('PG', 'PERUGIA'), ('PU', 'PESARO URBINO'), ('PE', 'PESCARA'), ('PC', 'PIACENZA'), ('PI', 'PISA'), ('PT', 'PISTOIA'), ('PN', 'PORDENONE'), ('PZ', 'POTENZA'), ('PO', 'PRATO'), ('RG', 'RAGUSA'), ('RA', 'RAVENNA'), ('RC', 'REGGIO CALABRIA'), ('RE', 'REGGIO EMILIA'), ('RI', 'RIETI'), ('RN', 'RIMINI'), ('ROMA', 'ROMA'), ('RO', 'ROVIGO'), ('SA', 'SALERNO'), ('SS', 'SASSARI'), ('SV', 'SAVONA'), ('SI', 'SIENA'), ('SR', 'SIRACUSA'), ('SO', 'SONDRIO'), ('TA', 'TARANTO'), ('TE', 'TERAMO'), ('TR', 'TERNI'), ('TO', 'TORINO'), ('TP', 'TRAPANI'), ('TN', 'TRENTO'), ('TV', 'TREVISO'), ('TS', 'TRIESTE'), ('UD', 'UDINE'), ('VA', 'VARESE'), ('VE', 'VENEZIA'), ('VB', 'VERBANIA'), ('VC', 'VERCELLI'), ('VR', 'VERONA'), ('VV', 'VIBO VALENTIA'), ('VI', 'VICENZA'), ('VT', 'VITERBO')], default='TO', help_text='Inserire la provincia operativa del medico', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Sesso',
            field=models.CharField(blank=True, choices=[('m', 'Maschio'), ('f', 'Femmina')], default='m', help_text='Sesso del medico', max_length=1),
        ),
    ]
