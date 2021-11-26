from django.forms import ModelForm

from equitymasterapp.models import Equity


class EquityCreationForm(ModelForm):
    class Meta:
        model = Equity
        fields = ['ticker', 'market', 'name', 'currency', 'image']