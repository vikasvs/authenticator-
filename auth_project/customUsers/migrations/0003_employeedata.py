# Generated by Django 3.0.6 on 2020-05-31 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUsers', '0002_auto_20200531_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=255)),
                ('your_email', models.EmailField(max_length=254)),
                ('offer_letter', models.FileField(upload_to='documents/')),
                ('role', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('manager_name', models.CharField(max_length=255)),
                ('manager_email', models.EmailField(max_length=254)),
                ('recruiter_name', models.CharField(max_length=255)),
                ('recruiter_email', models.EmailField(max_length=254)),
                ('form_completion', models.BooleanField(default=False)),
            ],
        ),
    ]
