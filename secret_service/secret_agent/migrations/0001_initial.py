# Generated by Django 5.0.4 on 2024-04-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('badge_no', models.CharField(max_length=10, unique=True)),
                ('code_name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=50)),
                ('secret_mission', models.TextField()),
                ('active', models.BooleanField()),
                ('no_of_assignments', models.IntegerField()),
            ],
        ),
    ]
