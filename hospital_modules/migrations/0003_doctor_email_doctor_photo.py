# Generated by Django 4.2.1 on 2023-06-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_modules', '0002_doctor_schedule_patient_doctor_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]