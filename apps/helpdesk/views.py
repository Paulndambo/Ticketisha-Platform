from django.shortcuts import render
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
    fields = "__all__"
    template_name = "helpdesk/new_ticket.html"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        description = request.POST.get("description")
        ticket_type = request.POST.get("ticket_type")
        customer = request.POST.get("customer")
        status = request.POST.get("status")
        screenshots = request.POST.get("screenshots")
        reporter = request.POST.get("reporter")
        
        print("************Ticket Title************")
        print(title)
        print(description)
        print("************Ticket Title************")
        return super().post(request, *args, **kwargs)

class TestCreate(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "helpdesk/test_create.html"