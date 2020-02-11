# Generated by Django 2.2.2 on 2020-02-07 11:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FactMag_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default=None, max_length=300)),
                ('headline', models.CharField(default=None, max_length=200, unique=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 2, 7, 11, 25, 52, 873121, tzinfo=utc))),
                ('is_highlight', models.CharField(default=None, max_length=1)),
                ('tags', models.CharField(default=None, max_length=200)),
                ('category', models.CharField(default=None, max_length=10)),
            ],
        ),
    ]
