# Generated by Django 3.2.9 on 2021-11-29 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equityownedapp', '0003_auto_20211128_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equityowned',
            name='average_purchase_price_mv',
        ),
    ]
