# Generated by Django 3.0.4 on 2020-04-04 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20200405_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 5, 0, 51, 15, 789316)),
        ),
    ]
