from django.urls import path
from .import views 

urlpatterns = [
    path("", views.tickets, name="tickets"),
    path("tickets-today/", views.today_tickets, name="tickets-today"),
    path("open-tickets/", views.open_tickets, name="open-tickets"),
    path("closed-tickets/", views.closed_tickets, name="closed-tickets"),
    path("new-ticket/", views.CreateNewTicket.as_view(), name="new-ticket"),
]