# Generated by Django 4.1.4 on 2023-02-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0025_laptop_rating_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirts',
            name='users',
            field=models.CharField(default='10', max_length=30),
        ),
        migrations.AddField(
            model_name='womens_clothes',
            name='users',
            field=models.CharField(default='10', max_length=30),
        ),
    ]
