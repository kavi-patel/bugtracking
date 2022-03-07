# Generated by Django 3.1.7 on 2022-02-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_establishment', models.DateField(blank=True, null=True)),
                ('official_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('logo', models.ImageField(blank=True, default=None, null=True, upload_to='company/company-logo/')),
            ],
        ),
    ]
