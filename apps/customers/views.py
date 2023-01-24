from django.shortcuts import render
from .models import Customer

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Create your views here.
def customers(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }
    return render(request, 'customers/customers.html', context)


class CreateNewCustomer(CreateView):
    model = Customer
    fields = "__all__"
    template_name = "customers/new_customer.html"