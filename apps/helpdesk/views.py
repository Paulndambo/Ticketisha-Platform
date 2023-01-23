from django.shortcuts import render
from .models import Ticket, TicketDiscussion
# Create your views here.
def tickets(request):
    tickets = Ticket.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, 'helpdesk/tickets.html', context)