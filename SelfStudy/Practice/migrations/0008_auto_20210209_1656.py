# Generated by Django 3.1.6 on 2021-02-09 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Practice', '0007_auto_20210209_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 16, 56, 20, 398007)),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 16, 56, 20, 398007)),
        ),
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 16, 56, 20, 398007)),
        ),
    ]
