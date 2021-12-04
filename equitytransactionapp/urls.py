from django.urls import path

from equitytransactionapp.views import EquityTransactionCreateView, EquityTransactionListView, \
    EquityTransactionDeleteView, import_csv, export_csv_template

app_name = 'equitytransactionapp'

urlpatterns = [

    path('create/',EquityTransactionCreateView.as_view(),name='create'),
    path('list/',EquityTransactionListView.as_view(),name='list'),
    path('delete/<int:pk>',EquityTransactionDeleteView.as_view(),name='delete'),

    path('import_csv/', import_csv, name='import_csv'),
    path('export_csv_template/', export_csv_template, name='export_csv_template'),
]