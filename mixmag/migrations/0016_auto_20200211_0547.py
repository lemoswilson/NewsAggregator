# Generated by Django 2.2.2 on 2020-02-11 05:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mixmag', '0015_auto_20200211_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mixmag_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 5, 47, 6, 512697, tzinfo=utc)),
        ),
    ]
