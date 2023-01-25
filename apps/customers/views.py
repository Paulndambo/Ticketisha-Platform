from django.shortcuts import render
from .models import Customer
from django.contrib.auth.models import User
from django.db import transaction

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

    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        website = request.POST.get('website')
        logo = request.POST.get('logo')
        postal_code = request.POST.get('postal_code')
        city = request.POST.get('city')
        country = request.POST.get('country')
        zip_code = request.POST.get('zip_code')
        headquarters = request.POST.get('headquarters')
        status = request.POST.get('status')

        customer_obj = f"""
        1. Name: {name}
        2. Email: {email}
        3. Phone: {phone_number}
        4. Website: {website}
        5. Logo: {logo}
        6. Address: {postal_code}, {city}-{country}
        7. HQ: {headquarters}
        8. Status: {status}
        """
        print(customer_obj)


        """Create A User Instance"""
        user = User()
        user.username = email
        user.email = email
        user.is_active = True
        user.is_staff = False
        user.set_password('1234')


        print(name)
        return super().post(request, *args, **kwargs)