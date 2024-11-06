# Generated by Django 4.0.6 on 2024-10-08 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('model', models.CharField(choices=[('model_a', 'Model A'), ('model_b', 'Model B'), ('model_c', 'Model C')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='bomdata.bom')),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(max_length=255)),
                ('make', models.CharField(choices=[('Pusher', 'Pusher'), ('Cumi', 'Cumi'), ('Cumi (Premier)', 'Cumi (Premier)'), ('Dimond', 'Dimond'), ('Fenner', 'Fenner'), ('Emarco', 'Emarco'), ('Nu Tech', 'Nu Tech'), ('Lovejoy', 'Lovejoy'), ('Audco', 'Audco'), ('NTN', 'NTN'), ('Raicer', 'Raicer'), ('Legris', 'Legris'), ('Delta', 'Delta'), ('Vanaz', 'Vanaz'), ('Avcon', 'Avcon'), ('IEPL', 'IEPL'), ('Champion Coolers', 'Champion Coolers'), ('Jhonson', 'Jhonson'), ('Auro', 'Auro'), ('Bharat Bijlee', 'Bharat Bijlee'), ('Rossi', 'Rossi'), ('SMC', 'SMC'), ('EP', 'EP'), ('HICARB', 'HICARB'), ('NILL', 'NIL'), ('indian', 'indian')], max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=100)),
                ('rate', models.CharField(default='0', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='bomdata.component')),
            ],
        ),
    ]
