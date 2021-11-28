from django.urls import path

from equitytransactionapp.views import EquityTransactionCreateView

app_name = 'equitytransactionapp'

urlpatterns = [

    path('create/',EquityTransactionCreateView.as_view(),name='create'),

]