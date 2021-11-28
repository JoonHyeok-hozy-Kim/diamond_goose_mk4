from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from equityownedapp.models import EquityOwned
from equitytransactionapp.models import EquityTransaction


class EquityTransactionCreateView(CreateView):
    model = EquityTransaction
    template_name = 'equitytransactionapp/create.html'

    def form_valid(self, form):
        temp_transaction = form.save(commit=False)
        temp_transaction.equity_owned = EquityOwned.get(pk=self.request.POST['equity_owned_pk'])
        temp_transaction.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('equityownedapp:detail',kwargs={'pk':self.object.equity_owned.pk})