# Generated by Django 4.2.1 on 2023-06-07 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_modules', '0004_patient_photo_alter_doctor_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('token', models.IntegerField()),
                ('Schedule', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital_modules.schedule')),
                ('patient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital_modules.patient')),
            ],
        ),
    ]
