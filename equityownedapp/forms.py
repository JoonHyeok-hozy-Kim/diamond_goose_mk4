from django.forms import ModelForm

from equityownedapp.models import EquityOwned


class EquityOwnedCreationForm(ModelForm):
    class Meta:
        model = EquityOwned
        fields = []

