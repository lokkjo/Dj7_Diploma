# Generated by Django 2.2.9 on 2020-02-06 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewed_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='goods.Item'),
        ),
        migrations.AddField(
            model_name='orderposition',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Item'),
        ),
        migrations.AddField(
            model_name='orderposition',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='покупатель'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='goods.OrderPosition', to='goods.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='review',
            field=models.ManyToManyField(related_name='items', through='goods.Review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.ItemType'),
        ),
    ]