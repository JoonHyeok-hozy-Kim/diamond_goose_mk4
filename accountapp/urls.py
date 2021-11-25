from django.urls import path

from accountapp.views import AccountCreateView, temp_welcome_view

app_name = "accountapp"

urlpatterns = [

    path('temp_welcome/',temp_welcome_view,name='temp_welcome'),

    path('create/',AccountCreateView.as_view(),name='create'),

]