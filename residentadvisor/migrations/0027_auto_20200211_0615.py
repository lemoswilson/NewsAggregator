# Generated by Django 2.2.2 on 2020-02-11 06:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('residentadvisor', '0026_auto_20200211_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residentadvisor_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 6, 15, 54, 326639, tzinfo=utc)),
        ),
    ]
