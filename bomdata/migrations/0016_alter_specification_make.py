# Generated by Django 4.0.6 on 2024-10-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bomdata', '0015_alter_specification_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='make',
            field=models.CharField(choices=[('Pusher', 'Pusher'), ('Cumi', 'Cumi'), ('Cumi (Premier)', 'Cumi (Premier)'), ('Dimond', 'Dimond'), ('Fenner', 'Fenner'), ('Emarco', 'Emarco'), ('Nu Tech', 'Nu Tech'), ('Lovejoy', 'Lovejoy'), ('Audco', 'Audco'), ('NTN', 'NTN'), ('Raicer', 'Raicer'), ('Legris', 'Legris'), ('Delta', 'Delta'), ('Vanaz', 'Vanaz'), ('Avcon', 'Avcon'), ('IEPL', 'IEPL'), ('Champion Coolers', 'Champion Coolers'), ('Jhonson', 'Jhonson'), ('Auro', 'Auro'), ('Bharat Bijlee', 'Bharat Bijlee'), ('Rossi', 'Rossi'), ('SMC', 'SMC'), ('EP', 'EP'), ('HICARB', 'HICARB'), ('NILL', 'NIL'), ('indian', 'indian'), ('JAISON', 'JAISON'), ('PMA', 'PMA'), ('Intact', 'Intact'), ('Drivetech', 'Drivetech'), ('Delton', 'Delton')], max_length=255),
        ),
    ]
