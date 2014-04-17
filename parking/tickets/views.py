from django.shortcuts import render
from django.http import HttpResponse
from tickets.models import Location, Reason, Ticket

def home(request):
    locations = Location.objects.order_by('location')
    return render(request, 'index.html', {'locations': locations})

def locationdetail(request, slug):
    loc = Location.objects.get(location_slug=slug)
    tickets = Ticket.objects.filter(location=loc) 
    return render(request, 'locationdetail.html', {'loc': loc, 'tickets': tickets})


