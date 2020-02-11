# Generated by Django 2.2.2 on 2020-02-10 09:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('factmag', '0003_auto_20200209_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factmag_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 10, 9, 7, 6, 718979, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='factmag_model',
            name='headline',
            field=models.CharField(default=None, max_length=300, unique=True),
        ),
    ]
