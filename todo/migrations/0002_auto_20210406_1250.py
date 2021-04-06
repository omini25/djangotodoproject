# Generated by Django 3.1.7 on 2021-04-06 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
