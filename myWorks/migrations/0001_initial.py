# Generated by Django 4.2.1 on 2023-05-31 18:00

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('technologies', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(default=None, max_length=255, verbose_name='images')),
            ],
        ),
    ]
