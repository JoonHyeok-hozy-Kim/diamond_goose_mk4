from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin

from equitymasterapp.models import Equity
from equityownedapp.decorator import equity_owned_ownership_required
from equityownedapp.forms import EquityOwnedCreationForm
from equityownedapp.models import EquityOwned
from equitytransactionapp.forms import EquityTransactionCreationForm

has_ownership = [login_required, equity_owned_ownership_required]


class EquityOwnedCreateView(CreateView):
    model = EquityOwned
    form_class = EquityOwnedCreationForm
    context_object_name = 'target_equity_owned'
    template_name = 'equityownedapp/create.html'

    def form_valid(self, form):
        temp_equityowned = form.save(commit=False)
        temp_equityowned.owner = self.request.user
        temp_equityowned.equity = Equity.objects.get(pk=self.request.POST['equity_pk'])
        temp_equityowned.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('equityownedapp:detail', kwargs={'pk':self.object.pk})


@method_decorator(has_ownership,'get')
class EquityOwnedDetailView(DetailView, FormMixin):
    model = EquityOwned
    form_class = EquityTransactionCreationForm
    context_object_name = 'target_equity_owned'
    template_name = 'equityownedapp/detail.html'


class EquityOwnedListView(ListView):
    model = EquityOwned
    context_object_name = 'equity_owned_list'
    template_name = 'equityownedapp/list.html'
