# Generated by Django 5.0.6 on 2024-05-22 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    # changes made to the database that future versions will depend on are placed here. 
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('telephone_number', models.IntegerField(max_length=10)),
                ('email_address', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('home_ownership', models.CharField(choices=[('OWN', 'Owns_Property'), ('RENT', 'Rents_Property')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Drivers_License', models.CharField(max_length=25)),
                ('Drivers_License_State', models.TextField(max_length=25)),
                ('gender', models.CharField(verbose_name=(('MALE', 'Male'), ('WOMAN', 'Woman'), ('NONBINARY', 'NonBinary')))),
                ('driving_experience', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_Identification_Number', models.CharField(max_length=17)),
                ('Usage_Type', models.CharField(blank=True, choices=[('PLEASURE', 'Pleasure Vehicle'), ('WORK', 'Work/School'), ('BUSINESS', 'Business'), ('COMMERCIAL', 'Commercial')], max_length=11)),
                ('Annual_Mileage', models.IntegerField()),
                ('Year', models.IntegerField()),
                ('Make', models.CharField(max_length=20)),
                ('Model', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reference_Number', models.CharField(max_length=25)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.customer')),
                ('Drivers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.drivers')),
                ('Vehicles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.vehicle')),
            ],
        ),
    ]