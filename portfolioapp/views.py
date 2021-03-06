from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin

from portfolioapp.forms import PortfolioCreationForm
from portfolioapp.models import Portfolio


class PortfolioCreateView(CreateView):
    model = Portfolio
    form_class = PortfolioCreationForm
    context_object_name = 'target_portfolio'
    template_name = 'portfolioapp/create.html'

    def form_valid(self, form):
        temp_portfolio = form.save(commit=False)
        temp_portfolio.owner = self.request.user
        temp_portfolio.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:temp_welcome')
        #return reverse('portfolioapp:detail', kwargs={'pk':self.object.pk})


class PortfolioDetailView(DetailView):
    model = Portfolio
    context_object_name = 'target_portfolio'
    template_name = 'portfolioapp/detail.html'