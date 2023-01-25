from django.urls import path 
from .import views 

urlpatterns = [
    path("", views.customers, name="customers"),
    path("new-customer/", views.CreateNewCustomer.as_view(), name="new-customer"),
]