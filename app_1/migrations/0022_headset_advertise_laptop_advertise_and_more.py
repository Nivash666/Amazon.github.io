# Generated by Django 4.1.4 on 2023-02-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0021_womens_clothes'),
    ]

    operations = [
        migrations.AddField(
            model_name='headset',
            name='advertise',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='advertise',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='mobile_depth',
            name='advertise',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='shirts',
            name='advertise',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='tv',
            name='advertise',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='womens_clothes',
            name='advertise',
            field=models.BooleanField(default='False'),
        ),
    ]