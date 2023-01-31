from django.db import models
from apps.customers.models import Customer
from apps.core.models import AbstractBaseModel
from django.conf import settings
from tinymce.models import HTMLField
from django.urls import reverse, reverse_lazy

# Create your models here.
content = HTMLField()
TICKET_TYPE_CHOICES = (
    ("bug", "Bug"),
    ("feature", "Feature"),
)

TICKET_STATUS_CHOICES = (
    ("reported", "Reported"),
    ("todo", "Todo"),
    ("in_progress", "In Progress"),
    ("done", "Done"),
    ("blocked", "Blocked"),
)

class Ticket(AbstractBaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    ticket_type = models.CharField(max_length=255, choices=TICKET_TYPE_CHOICES)
    #description = models.TextField()
    description = HTMLField()
    status = models.CharField(max_length=255, choices=TICKET_STATUS_CHOICES)
    screenshots = models.ImageField(upload_to="screenshots/", null=True, blank=True)
    reporter = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tickets')



class TicketDiscussion(AbstractBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    message = models.TextField(blank=True)
    files = models.FileField(upload_to="ticket_files", null=True, blank=True)

    def __str__(self):
        return self.user.username