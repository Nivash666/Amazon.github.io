# Generated by Django 4.1.4 on 2023-02-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0020_alter_laptop_os_alter_laptop_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Womens_clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('head', models.CharField(max_length=200)),
                ('discount_price', models.CharField(max_length=10)),
                ('orginal_price', models.CharField(max_length=10)),
                ('discount', models.CharField(max_length=10)),
                ('rating_img', models.ImageField(default='pics', upload_to='pics')),
                ('day', models.CharField(default='10', max_length=10)),
                ('date', models.IntegerField(default=1)),
                ('int_dicount_price', models.IntegerField()),
                ('int_orginal_price', models.IntegerField()),
                ('women_model', models.CharField(max_length=100)),
                ('type', models.CharField(default='womens_clothes', max_length=20)),
            ],
        ),
    ]
