# Generated by Django 4.0.5 on 2022-06-20 06:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_datebirth_user_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_filled_up',
            field=models.DateField(default=datetime.datetime(2022, 6, 20, 6, 51, 58, 189869, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 6, 20, 6, 51, 58, 189869, tzinfo=utc)),
        ),
    ]
