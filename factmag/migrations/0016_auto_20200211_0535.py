# Generated by Django 2.2.2 on 2020-02-11 05:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('factmag', '0015_auto_20200211_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factmag_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 5, 35, 55, 986375, tzinfo=utc)),
        ),
    ]
