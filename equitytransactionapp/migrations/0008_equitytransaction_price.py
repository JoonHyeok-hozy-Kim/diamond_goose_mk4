# Generated by Django 3.2.9 on 2021-11-29 04:08

from django.db import migrations
import equitytransactionapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('equitytransactionapp', '0007_alter_equitytransaction_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='equitytransaction',
            name='price',
            field=equitytransactionapp.models.MinValueFloat(default=0),
        ),
    ]
