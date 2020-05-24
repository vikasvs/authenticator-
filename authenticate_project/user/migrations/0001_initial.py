# Generated by Django 2.1.5 on 2020-05-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
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
            ],
        ),
    ]
