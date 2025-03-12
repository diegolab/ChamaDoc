import random
import string

from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render

from .forms import AssignTicketForm, CreateTicketForm
from .models import Ticket


def create_ticket(request):
    if request.method == "POST":
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            while not var.ticket_id:
                id = "".join(random.choices(string.digits, k=6))
                try:
                    var.ticket_id = id
                    var.save()
                    break
                except IntegrityError:
                    continue
            messages.success(request, "Ticket created successfully")
            return redirect("customer-tickets")
        else:
            messages.error(request, "Invalid form data")
            return redirect("create-ticket")
    else:
        form = CreateTicketForm()
        return render(request, "ticket/create_ticket.html", {"form": form})


def customer_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user)
    return render(request, "ticket/customer_tickets.html", {"tickets": tickets})


def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == "POST":
        form = AssignTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_assigned_to_engineer = True
            var.save()
            messages.success(request, f"Ticket assigned successfully to {var.engineer}")
            return redirect("ticket-queue")
        else:
            messages.error(request, "Invalid form data")
            return redirect("assign-ticket", ticket_id=ticket_id)
    else:
        form = AssignTicketForm()
        return render(request, "ticket/assign_ticket.html", {"form": form})


def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    return render(request, "ticket/ticket_details.html", {"ticket": ticket})


def ticket_queue(request):
    tickets = Ticket.objects.filter(is_assigned_to_engineer=False)
    return render(request, "ticket/ticket_queue.html", {"tickets": tickets})
