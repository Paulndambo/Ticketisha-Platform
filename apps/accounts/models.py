from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import AbstractBaseModel
# Create your models here.

from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, AbstractBaseModel):
    ROLE_INDIVIDUAL = "individual"

    ROLE_CHOICES = (
        ('None', 'Without role'),
        ('admin', 'C2S Admin'),
        ('insurer', 'Insurer'),
        ('corporate', 'Corporate'),
        ('merchant', 'Merchant'),
        (ROLE_INDIVIDUAL, 'Individual'),
        ('report_user', 'Report User'),
        ('technician_user', 'Technician User'),
        ('foh_user', 'FOH User'),
        ('customer_support_user', 'Customer Support User'),
        ('funeral_validator', 'Funeral Validator'),
        ('brokerage_admin', 'Brokerage Admin'),
        ('broker', 'Broker'),
        ('claim_validator', 'Claim Validator'),
        ('retail_agent', 'Retail Agent'),
    )
   
    token = models.CharField(null=True, max_length=255)
    token_expiration_date = models.DateTimeField(null=True)
    activation_date = models.DateTimeField(null=True)
    email = models.EmailField(unique=True, error_messages={'unique': _('A user with that email already exists.')})
    role = models.CharField(choices=ROLE_CHOICES, max_length=32)
    password_expiration_date = models.DateField(null=True)
    reset_password = models.BooleanField(default=False)
