# Generated by Django 4.2.1 on 2023-06-06 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=100)),
                ('gender', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('login_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital_modules.login')),
            ],
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('starting_time', models.CharField(max_length=200)),
                ('ending_time', models.CharField(max_length=200)),
                ('total_token', models.CharField(max_length=200)),
                ('doctor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital_modules.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=100)),
                ('gender', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('login_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital_modules.login')),
            ],
        ),
        migrations.CreateModel(
            name='doctor_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(max_length=100)),
                ('date', models.CharField(max_length=200)),
                ('doctor_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital_modules.doctor')),
                ('patient_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital_modules.patient')),
            ],
        ),
    ]
