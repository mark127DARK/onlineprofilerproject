# Generated by Django 4.0.5 on 2022-06-20 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_fname', models.CharField(max_length=255, verbose_name='First Name')),
                ('user_lname', models.CharField(max_length=255, verbose_name='Last Name')),
                ('user_mi', models.CharField(max_length=25, verbose_name='M.I')),
                ('user_email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('user_position', models.CharField(max_length=255, verbose_name='Position Title')),
                ('datebirth', models.DateField(default=datetime.datetime(2022, 6, 20, 6, 17, 44, 884471, tzinfo=utc))),
                ('user_area', models.CharField(max_length=255, verbose_name='Area of Assignment')),
                ('user_training', models.CharField(max_length=255, verbose_name='Training Attended')),
                ('user_venue', models.CharField(max_length=255, verbose_name='Venue')),
                ('user_image', models.ImageField(default='profile_pic/image.jpg', upload_to=users.models.image_path)),
                ('pub_date', models.DateField(default=datetime.datetime(2022, 6, 20, 6, 17, 44, 884471, tzinfo=utc))),
            ],
        ),
    ]