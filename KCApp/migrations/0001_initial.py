# Generated by Django 4.2.5 on 2023-11-06 08:30

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listingcatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=200, null=True)),
                ('Make', models.CharField(max_length=200, null=True)),
                ('CarModel', models.CharField(max_length=200, null=True)),
                ('Year', models.IntegerField(null=True)),
                ('Odometer', models.IntegerField(null=True)),
                ('BodyStyle', models.CharField(max_length=200, null=True)),
                ('Transmission', models.CharField(max_length=200, null=True)),
                ('FuelType', models.CharField(max_length=200, null=True)),
                ('EngineSize', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('DriveType', models.CharField(max_length=200, null=True)),
                ('ExteriorColor', models.CharField(max_length=200, null=True)),
                ('Doors', models.IntegerField(null=True)),
                ('New', models.BooleanField(null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('WOF', models.BooleanField(null=True)),
                ('Registration', models.BooleanField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=200, null=True)),
                ('CloudImage', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='KCApp.listingcatagory')),
            ],
        ),
    ]
