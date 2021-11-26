from django.urls import path

from equitymasterapp.views import EquityListView, EquityCreateView, EquityDetailView

app_name = 'equitymasterapp'

urlpatterns = [

    path('list/',EquityListView.as_view(),name='list'),
    path('create/',EquityCreateView.as_view(),name='create'),
    path('detail/<int:pk>',EquityDetailView.as_view(),name='detail'),

]