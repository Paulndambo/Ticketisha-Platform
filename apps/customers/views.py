from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import *
from .models import *
from apps.accounts.models import *
# Create your views here.

def customers(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        print(status)
        if status == 'none':
            customers = Customer.objects.all()
        else:
            customers = Customer.objects.filter(status=status)
    else:
        customers = Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, 'customers/customers.html', context)


def create_customer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        website = request.POST.get('website')
        logo = request.POST.get('logo')
        postal_code = request.POST.get('postal_code')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city')
        country = request.POST.get('country')
        headquarters = request.POST.get('headquarters')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('new-customer')

        elif Customer.objects.filter(name=name).exists():
            messages.info(request, 'Name already exists')
            return redirect('new-customer')
        else:
            with transaction.atomic():
                user = User.objects.create_user(email=email, username=email)
                customer = Customer.objects.create(user=user, name=name, phone_number=phone_number, website=website, logo=logo, postal_code=postal_code, zip_code=zip_code, city=city, country=country, headquarters=headquarters)
    

            messages.success(request, 'Customer Created Successfully')
            return redirect('customers')

    else:
        return render(request, 'customers/add_customer.html')

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)

    context = {
        "customer": customer
    }

    return render(request, "customers/customer_detail.html", context)

class UpdateCustomerView(UpdateView):
    model = Customer
    fields = ['name', 'phone_number', 'website', 'logo', 'postal_code', 'zip_code', 'city', 'country', 'headquarters']
    template_name = 'customers/update_customer.html'

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()

    return redirect('customers')