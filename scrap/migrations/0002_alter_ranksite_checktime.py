# Generated by Django 4.2.4 on 2023-08-21 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranksite',
            name='checkTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 15, 40, 46, 337646)),
        ),
    ]
