# Generated by Django 4.1.4 on 2023-02-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0024_rename_shirt_model_shirts_fashion_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='rating_img',
            field=models.ImageField(default='pics', upload_to='pics'),
        ),
    ]
