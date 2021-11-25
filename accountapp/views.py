from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView

def temp_welcome_view(request):
    return render(request, 'accountapp/temp_welcome.html')

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:temp_welcome')
    template_name = 'accountapp/create.html'