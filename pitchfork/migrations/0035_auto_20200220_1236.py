# Generated by Django 2.2.2 on 2020-02-20 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pitchfork', '0034_auto_20200211_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchfork_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 12, 36, 57, 87094, tzinfo=utc)),
        ),
    ]
