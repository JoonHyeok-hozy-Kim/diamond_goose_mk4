# Generated by Django 3.2.9 on 2021-11-28 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equitytransactionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equitytransaction',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.date(2021, 11, 28)),
        ),
        migrations.AlterField(
            model_name='equitytransaction',
            name='transaction_type',
            field=models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL'), ('DIVIDEND', 'DIVIDEND'), ('SPLIT_REMOVE', 'SPLIT_REMOVE'), ('SPLIT_ADD', 'SPLIT_ADD')], max_length=20),
        ),
    ]
