# Generated by Django 2.2.9 on 2020-02-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20200201_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtype',
            name='name',
            field=models.CharField(default='NewName', max_length=32),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
