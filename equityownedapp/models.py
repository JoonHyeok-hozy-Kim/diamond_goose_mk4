from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from equitymasterapp.models import Equity


class EquityOwned(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equity_owned', null=False)
    equity = models.ForeignKey(Equity, on_delete=models.SET_NULL, related_name='equity_owned', null=True)

    quantity = models.FloatField(default=0, null=False)
    average_purchase_price_mv = models.FloatField(default=0, null=False)
    average_purchase_price_fifo = models.FloatField(default=0, null=False)

    creation_date = models.DateTimeField(auto_now=True)
    last_update_date = models.DateTimeField(auto_now_add=True)