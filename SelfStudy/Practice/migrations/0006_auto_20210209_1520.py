# Generated by Django 3.1.6 on 2021-02-09 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Practice', '0005_auto_20210205_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 15, 20, 55, 578889)),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 15, 20, 55, 578889)),
        ),
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 15, 20, 55, 578889)),
        ),
    ]