# Generated by Django 4.1.4 on 2023-02-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0006_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='type',
            field=models.CharField(default='laptop', max_length=20),
        ),
        migrations.AddField(
            model_name='mobile_depth',
            name='type',
            field=models.CharField(default='mobile', max_length=20),
        ),
        migrations.AddField(
            model_name='shirts',
            name='type',
            field=models.CharField(default='shirts', max_length=20),
        ),
        migrations.AddField(
            model_name='tv',
            name='type',
            field=models.CharField(default='tv', max_length=20),
        ),
    ]