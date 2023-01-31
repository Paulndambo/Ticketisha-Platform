from django.contrib import admin
from .models import Ticket, TicketDiscussion
# Register your models here.
admin.site.register(TicketDiscussion)
admin.site.register(Ticket)