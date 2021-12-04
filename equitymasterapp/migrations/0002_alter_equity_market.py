# Generated by Django 3.2.9 on 2021-11-29 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equitymasterapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equity',
            name='market',
            field=models.CharField(choices=[('KSE', 'Korean Stock Exchange'), ('NASDAQ', 'NASDAQ'), ('NYSE', 'NewYork Stock Exchange')], max_length=20),
        ),
    ]