# Generated by Django 3.2.9 on 2021-11-29 01:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equitytransactionapp', '0005_equitytransaction_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equitytransaction',
            name='quantity',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]