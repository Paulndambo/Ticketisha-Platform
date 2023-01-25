from django.urls import path 
from .import views 

urlpatterns = [
    path("", views.customers, name="customers"),
    path("customer-detail/<int:id>/", views.customer_detail, name="customer-details"),
    path("new-customer/", views.create_customer, name="new-customer"),
    path("update-customer/<int:pk>/", views.UpdateCustomerView.as_view(), name="update-customer"),
    path("delete-customer/<int:pk>/", views.delete_customer, name="delete-customer")
]