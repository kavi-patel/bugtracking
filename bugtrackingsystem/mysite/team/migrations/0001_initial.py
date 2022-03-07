# Generated by Django 3.1.7 on 2022-02-24 05:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default='Team Description', max_length=500)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]