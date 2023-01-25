from django.urls import path 
from .import views 

urlpatterns = [
    path("", views.customers, name="customers"),
    path("new-customer/", views.create_customer, name="new-customer"),
]