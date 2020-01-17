# Generated by Django 3.0 on 2019-12-16 08:49

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='driving_licence',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='D:\\ChampionzArena\\championzarena\\DOCS'), upload_to='uploads/driving_licence/DL14-17-23'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_driving_licence_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_pancard_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pancard',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='D:\\ChampionzArena\\championzarena\\DOCS'), upload_to='uploads/pancard/pancard14-17-23'),
        ),
    ]
