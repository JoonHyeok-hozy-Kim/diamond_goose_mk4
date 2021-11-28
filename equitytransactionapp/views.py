from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from equityownedapp.models import EquityOwned
from equitytransactionapp.decorator import equity_transaction_ownership_required
from equitytransactionapp.forms import EquityTransactionCreationForm
from equitytransactionapp.models import EquityTransaction

has_ownership = [login_required, equity_transaction_ownership_required]


class EquityTransactionCreateView(CreateView):
    model = EquityTransaction
    form_class = EquityTransactionCreationForm
    template_name = 'equitytransactionapp/create.html'

    def form_valid(self, form):
        temp_transaction = form.save(commit=False)
        temp_transaction.equity_owned = EquityOwned.objects.get(pk=self.request.POST['equity_owned_pk'])
        temp_transaction.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('equityownedapp:detail',kwargs={'pk':self.object.equity_owned.pk})


class EquityTransactionListView(ListView):
    model = EquityTransaction
    context_object_name = 'equity_transaction_list'
    template_name = 'equitytransactionapp/list.html'