# Generated by Django 4.0.6 on 2022-11-02 07:50

import datetime
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
                ('messagetext', models.CharField(max_length=10000)),
                ('username', models.CharField(max_length=1000)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('messageroom', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(max_length=1000)),
            ],
        ),
    ]