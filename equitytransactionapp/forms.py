from django.forms import widgets
from django.forms import ModelForm

from equitytransactionapp.models import EquityTransaction


class EquityTransactionCreationForm(ModelForm):
    class Meta:
        model = EquityTransaction
        fields = ['transaction_type', 'quantity', 'purchase_price', 'transaction_fee', 'transaction_tax', 'transaction_date', 'note']

        widgets = {
            'transaction_date': widgets.DateTimeInput(attrs={'type':'date'})
        }