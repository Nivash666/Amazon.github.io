# Generated by Django 4.1.4 on 2023-02-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0014_browsing_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='headset',
            name='date',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='headset',
            name='day',
            field=models.CharField(default='10', max_length=10),
        ),
        migrations.AddField(
            model_name='headset',
            name='rating_img',
            field=models.ImageField(default='pics', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='shirts',
            name='date',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='shirts',
            name='day',
            field=models.CharField(default='10', max_length=10),
        ),
        migrations.AddField(
            model_name='shirts',
            name='rating_img',
            field=models.ImageField(default='pics', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='tv',
            name='date',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tv',
            name='day',
            field=models.CharField(default='10', max_length=10),
        ),
        migrations.AddField(
            model_name='tv',
            name='rating_img',
            field=models.ImageField(default='pics', upload_to='pics'),
        ),
    ]
