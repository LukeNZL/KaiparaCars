# Generated by Django 4.2.5 on 2023-10-25 01:10

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KCApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listingcatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='listing',
            name='Images',
        ),
        migrations.AddField(
            model_name='listing',
            name='CloudImage',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='listing',
            name='CreatedBy',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='BodyStyle',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='CarModel',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Doors',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='DriveType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='EngineSize',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='ExteriorColor',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='FuelType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Make',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='New',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Odometer',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Registration',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Title',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Transmission',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='WOF',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='KCApp.listingcatagory'),
        ),
    ]