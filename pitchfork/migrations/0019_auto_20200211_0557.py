# Generated by Django 2.2.2 on 2020-02-11 05:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pitchfork', '0018_auto_20200211_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchfork_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 5, 57, 33, 2227, tzinfo=utc)),
        ),
    ]
