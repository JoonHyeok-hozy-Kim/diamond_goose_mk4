from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from copy import deepcopy

# Create your models here.
from equitymasterapp.models import Equity


class EquityOwned(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equity_owned', null=False)
    equity = models.ForeignKey(Equity, on_delete=models.SET_NULL, related_name='equity_owned', null=True)

    quantity = models.FloatField(default=0, null=False)
    average_purchase_price_mv = models.FloatField(default=0, null=False)
    average_purchase_price_fifo = models.FloatField(default=0, null=False)

    rate_of_return_mv = models.FloatField(default=0, null=False)
    rate_of_return_fifo = models.FloatField(default=0, null=False)

    creation_date = models.DateTimeField(auto_now=True)
    last_update_date = models.DateTimeField(auto_now_add=True)

    @property
    def quantity(self):
        query = Q(transaction_type='BUY')
        query.add(Q(transaction_type='SELL'),Q.OR)
        query.add(Q(quantity__gt=0),Q.AND)
        query.add(Q(split_flag=False),Q.AND)

        transaction_data_set = self.transaction.filter(query).values()
        result = 0

        for transaction_data in transaction_data_set:
            if transaction_data['transaction_type'] == 'BUY':
                result += transaction_data['quantity']
            else:
                result -= transaction_data['quantity']

        return result

    @property
    def average_purchase_price_mv(self):
        query = Q(transaction_type='BUY')
        query.add(Q(transaction_type='SELL'),Q.OR)
        query.add(Q(quantity__gt=0),Q.AND)
        query.add(Q(split_flag=False),Q.AND)

        transaction_data_set = self.transaction.filter(query).order_by('transaction_date').values()
        temp_qty = 0
        temp_amt = 0

        for transaction_data in transaction_data_set:
            if transaction_data['transaction_type'] == 'BUY':
                temp_qty += transaction_data['quantity']
                temp_amt += transaction_data['quantity'] * transaction_data['price']
            else:
                temp_price = temp_amt/temp_qty
                temp_qty -= transaction_data['quantity']
                temp_amt = temp_qty * temp_price

        if temp_qty < 0: result = -999
        elif temp_qty == 0: result = 0
        else: result = temp_amt/temp_qty

        return result

    @property
    def average_purchase_price_fifo(self):
        query = Q(transaction_type='BUY')
        query.add(Q(transaction_type='SELL'),Q.OR)
        query.add(Q(quantity__gt=0),Q.AND)
        query.add(Q(split_flag=False),Q.AND)

        transaction_data_set = self.transaction.filter(query).order_by('transaction_date').values()
        transaction_amount_list = []
        temp_qty = 0
        temp_amt = 0

        for transaction_data in transaction_data_set:
            if transaction_data['transaction_type'] == 'BUY':
                for i in range(int(transaction_data['quantity'])):
                    transaction_amount_list.append(transaction_data['price'])
            else:
                for i in range(int(transaction_data['quantity'])):
                    transaction_amount_list.pop(0)

        for transaction_amount in transaction_amount_list:
            temp_qty += 1
            temp_amt += transaction_amount

        if temp_qty > 0: result = temp_amt/temp_qty
        else: result = 0

        return result

    @property
    def rate_of_return_mv(self):
        result = 0
        if self.average_purchase_price_mv > 0:
            result = (self.equity.current_price - self.average_purchase_price_mv)/self.average_purchase_price_mv
        return result

    @property
    def rate_of_return_fifo(self):
        result = 0
        if self.average_purchase_price_fifo > 0:
            result = (self.equity.current_price - self.average_purchase_price_fifo)/self.average_purchase_price_fifo
        return result
