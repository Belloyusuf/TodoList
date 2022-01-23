# Generated by Django 3.2.9 on 2021-12-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Student First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Student Last Name')),
                ('age', models.DateField(verbose_name='Date Of Birth')),
                ('gender', models.CharField(max_length=10, verbose_name='Student Gender')),
                ('address', models.TextField(verbose_name='Student Address')),
                ('disablity', models.BooleanField(default=False, verbose_name='Student Disability')),
                ('admission_date', models.DateTimeField(auto_now_add=True, verbose_name='Student admission Date Time')),
            ],
            options={
                'ordering': ['-admission_date'],
            },
        ),
    ]
