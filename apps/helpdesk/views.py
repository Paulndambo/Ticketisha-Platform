from django.shortcuts import render, redirect
from .models import Ticket, TicketDiscussion
from django.views.generic import CreateView, ListView, DeleteView, ListView
from .forms import TicketForm
# Create your views here.
def tickets(request):
    tickets = Ticket.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, 'helpdesk/tickets.html', context)


def today_tickets(request):
    tickets = Ticket.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, 'helpdesk/tickets.html', context)


def open_tickets(request):
    tickets = Ticket.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, 'helpdesk/tickets.html', context)


def closed_tickets(request):
    tickets = Ticket.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, 'helpdesk/tickets.html', context)



class CreateNewTicket(CreateView):
    model = Ticket
    fields = ['title', 'ticket_type', 'customer', 'reporter', 'description', 'screenshots']
    template_name = "helpdesk/new_ticket.html"



class TestCreate(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "helpdesk/test_create.html"