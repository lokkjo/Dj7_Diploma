# Generated by Django 2.2.9 on 2020-02-05 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200204_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderposition',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderposition',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderPosition',
        ),
    ]
