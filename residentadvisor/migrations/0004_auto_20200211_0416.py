# Generated by Django 2.2.2 on 2020-02-11 04:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('residentadvisor', '0003_auto_20200211_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residentadvisor_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 4, 16, 47, 161278, tzinfo=utc)),
        ),
    ]
