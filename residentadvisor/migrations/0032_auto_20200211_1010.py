# Generated by Django 2.2.2 on 2020-02-11 10:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('residentadvisor', '0031_auto_20200211_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='residentadvisor_model',
            old_name='is_featured',
            new_name='featured',
        ),
        migrations.AlterField(
            model_name='residentadvisor_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 10, 10, 11, 150073, tzinfo=utc)),
        ),
    ]
