# Generated by Django 2.2.9 on 2020-02-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20200201_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='media/photos/'),
        ),
    ]
