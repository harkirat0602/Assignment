# Generated by Django 5.0.2 on 2024-02-23 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=20)),
                ('km_price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Price_Calc.item')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Price_Calc.organization')),
            ],
        ),
    ]
