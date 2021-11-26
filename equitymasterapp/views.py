from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from equitymasterapp.models import Equity


class EquityListView(ListView):
    model = Equity
    template_name = 'equitymasterapp/list.html'


class EquityCreateView(CreateView):
    model = Equity
    fields = ['ticker', 'market', 'name', 'currency', 'image']
    context_object_name = 'equity_list'
    template_name = 'equitymasterapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:temp_welcome')


class EquityDetailView(DetailView):
    model = Equity
    context_object_name = 'target_equity'
    template_name = 'equitymasterapp/detail.html'