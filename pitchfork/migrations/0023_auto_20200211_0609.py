# Generated by Django 2.2.2 on 2020-02-11 06:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pitchfork', '0022_auto_20200211_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchfork_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 6, 9, 2, 65557, tzinfo=utc)),
        ),
    ]
