from django import forms

from .models import*

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'website', 'logo', 'postal_code', 'zip_code', 'city', 'country', 'headquarters']