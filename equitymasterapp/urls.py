from django.urls import path

from equitymasterapp.views import EquityListView, EquityCreateView, EquityDetailView, EquityUpdateView, EquityDeleteView

app_name = 'equitymasterapp'

urlpatterns = [

    path('list/',EquityListView.as_view(),name='list'),
    path('create/',EquityCreateView.as_view(),name='create'),
    path('detail/<int:pk>',EquityDetailView.as_view(),name='detail'),
    path('update/<int:pk>',EquityUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',EquityDeleteView.as_view(),name='delete'),

]