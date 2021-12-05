from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from equitymasterapp.forms import EquityCreationForm
from equitymasterapp.models import Equity
from equityownedapp.forms import EquityOwnedCreationForm
from equityownedapp.models import EquityOwned


class EquityListView(ListView):
    model = Equity
    template_name = 'equitymasterapp/list.html'


class EquityCreateView(CreateView):
    model = Equity
    form_class = EquityCreationForm
    context_object_name = 'equity_list'
    template_name = 'equitymasterapp/create.html'

    def get_success_url(self):
        return reverse('equitymasterapp:detail',kwargs={'pk':self.object.pk})


class EquityDetailView(DetailView,FormMixin):
    model = Equity
    form_class = EquityOwnedCreationForm
    context_object_name = 'target_equity'
    template_name = 'equitymasterapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(EquityDetailView, self).get_context_data(**kwargs)

        equity_owned_pk = None
        equity_owned_scalar_query = EquityOwned.objects.filter(owner=self.request.user, equity=self.object).values()
        if equity_owned_scalar_query:
            equity_owned_pk = equity_owned_scalar_query[0]['id']
        context.update({'equity_owned_pk': equity_owned_pk})

        return context

class EquityUpdateView(UpdateView):
    model = Equity
    form_class = EquityCreationForm
    context_object_name = 'target_equity'
    template_name = 'equitymasterapp/update.html'

    def get_success_url(self):
        return reverse('equitymasterapp:detail',kwargs={'pk':self.object.pk})


class EquityDeleteView(DeleteView):
    model = Equity
    context_object_name = 'target_equity'
    template_name = 'equitymasterapp/delete.html'

    def get_success_url(self):
        return reverse('equitymasterapp:list')