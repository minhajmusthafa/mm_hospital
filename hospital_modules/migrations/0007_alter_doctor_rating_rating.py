# Generated by Django 4.2.1 on 2023-07-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_modules', '0006_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_rating',
            name='rating',
            field=models.CharField(max_length=200),
        ),
    ]