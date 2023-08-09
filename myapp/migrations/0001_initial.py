# Generated by Django 4.2.3 on 2023-08-08 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('contect', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='attendance_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Type', models.CharField(max_length=25)),
                ('emp_id', models.ForeignKey(db_column='emp_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
            options={
                'db_table': 'attendance_table',
            },
        ),
    ]
