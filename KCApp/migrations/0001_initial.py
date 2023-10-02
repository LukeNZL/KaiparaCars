# Generated by Django 4.2.5 on 2023-10-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=200)),
                ('Images', models.ImageField(upload_to='images/')),
                ('Make', models.CharField(max_length=200)),
                ('CarModel', models.CharField(max_length=200)),
                ('Year', models.IntegerField(default=0)),
                ('Odometer', models.IntegerField(default=0)),
                ('BodyStyle', models.CharField(max_length=200)),
                ('Transmission', models.CharField(max_length=200)),
                ('FuelType', models.CharField(max_length=200)),
                ('EngineSize', models.IntegerField(default=0)),
                ('DriveType', models.CharField(max_length=200)),
                ('ExteriorColor', models.CharField(max_length=200)),
                ('Doors', models.IntegerField(default=0)),
                ('Condition', models.BooleanField()),
                ('Price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('WOF', models.BooleanField()),
                ('Registration', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
