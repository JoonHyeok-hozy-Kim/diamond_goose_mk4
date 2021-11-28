from django.urls import path

from equityownedapp.views import EquityOwnedCreateView, EquityOwnedDetailView, EquityOwnedListView

app_name = 'equityownedapp'

urlpatterns = [

    path('create/',EquityOwnedCreateView.as_view(), name='create'),
    path('detail/<int:pk>',EquityOwnedDetailView.as_view(), name='detail'),
    path('list/',EquityOwnedListView.as_view(), name='list'),

]