from django.urls import path

from equitytransactionapp.views import EquityTransactionCreateView, EquityTransactionListView

app_name = 'equitytransactionapp'

urlpatterns = [

    path('create/',EquityTransactionCreateView.as_view(),name='create'),
    path('list/',EquityTransactionListView.as_view(),name='list'),

]