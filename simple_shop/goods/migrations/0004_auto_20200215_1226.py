# Generated by Django 2.2.9 on 2020-02-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20200212_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='display_name',
            field=models.CharField(default='NewName', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='slug',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]