# Generated by Django 3.2.9 on 2021-11-29 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equitytransactionapp', '0008_equitytransaction_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equitytransaction',
            name='purchase_price',
            field=models.FloatField(default=0),
        ),
    ]
