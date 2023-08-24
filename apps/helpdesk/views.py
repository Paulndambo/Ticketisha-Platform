from django.shortcuts import render, redirect
from .models import Ticket, TicketDiscussion
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import TicketForm
# Create your views here.
def tickets(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        print(status)
        if status == 'none':
            tickets = Ticket.objects.all()
        else:
            tickets = Ticket.objects.filter(status=status)

    else:
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

def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)

    context = {
        'ticket': ticket
    }

    return render(request, 'helpdesk/ticket_detail.html', context)

class UpdateTicket(UpdateView):
    model = Ticket
    fields = ['title', 'ticket_type', 'customer', 'reporter', 'screenshots']
    template_name = "helpdesk/ticket_update.html"

def delete_ticket(request, id):
    ticket = Ticket.objects.get(id=id)

    ticket.delete()

    return redirect('tickets')


class TestCreate(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "helpdesk/test_create.html"