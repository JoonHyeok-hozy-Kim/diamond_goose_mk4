from django.urls import path

from equitytransactionapp.views import EquityTransactionCreateView, EquityTransactionListView, \
    EquityTransactionDeleteView

app_name = 'equitytransactionapp'

urlpatterns = [

    path('create/',EquityTransactionCreateView.as_view(),name='create'),
    path('list/',EquityTransactionListView.as_view(),name='list'),
    path('delete/<int:pk>',EquityTransactionDeleteView.as_view(),name='delete'),

]