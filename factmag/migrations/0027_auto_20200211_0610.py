# Generated by Django 2.2.2 on 2020-02-11 06:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('factmag', '0026_auto_20200211_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factmag_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 6, 10, 42, 938124, tzinfo=utc)),
        ),
    ]
