from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Portfolio(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    current_value = models.FloatField(default=0, null=False)

    capital_gain = models.FloatField(default=0, null=False)
    rate_of_return = models.FloatField(default=0, null=False)

    capital_gain_exchange_adjusted = models.FloatField(default=0, null=False)
    rate_of_return_exchange_adjusted = models.FloatField(default=0, null=False)

    mkt_ex_rate_usd_krw = models.FloatField(null=True)
    user_ex_rate_usd_krw = models.FloatField(null=True)