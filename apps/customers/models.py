from django.db import models
from django.conf import settings
from apps.core.models import AbstractBaseModel
from django.urls import reverse, reverse_lazy
# Create your models here.
CUSTOMER_STATUS_CHOICES = (
    ("active", "Active"),
    ("disabled", "Disabled"),
)

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    website = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to="customer_logos", null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    headquarters = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, default="active")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customers')