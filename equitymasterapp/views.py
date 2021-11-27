from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from equitymasterapp.forms import EquityCreationForm
from equitymasterapp.models import Equity


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


class EquityDetailView(DetailView):
    model = Equity
    context_object_name = 'target_equity'
    template_name = 'equitymasterapp/detail.html'


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