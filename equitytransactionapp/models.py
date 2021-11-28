from django.db import models
from django import utils

# Create your models here.
from django.forms.widgets import DateTimeInput
from django.forms import MultipleChoiceField, CheckboxSelectMultiple

from equityownedapp.models import EquityOwned

TRANSACTION_TYPE_CHOICES = (
    ('BUY', '매수'),
    ('SELL', '매도'),
    ('DIVIDEND', '배당금'),
    ('SPLIT', '액면분할'),
)

class EquityTransaction(models.Model):
    equity_owned = models.ForeignKey(EquityOwned, on_delete=models.CASCADE, related_name='transaction', null=False)

    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES, null=False)
    quantity = models.FloatField(null=False)
    purchase_price = models.FloatField(null=False)
    transaction_fee = models.FloatField(default=0)
    transaction_tax = models.FloatField(default=0)
    transaction_date = models.DateTimeField(default=utils.timezone.now, null=False)

    creation_date = models.DateTimeField(auto_now=True)
    last_update_date = models.DateTimeField(auto_now_add=True)



