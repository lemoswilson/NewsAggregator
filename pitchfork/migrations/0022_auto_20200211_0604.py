# Generated by Django 2.2.2 on 2020-02-11 06:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pitchfork', '0021_auto_20200211_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchfork_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 6, 4, 33, 873060, tzinfo=utc)),
        ),
    ]