from django.shortcuts import render
from django.http import HttpResponse
from tickets.models import Location, Reason, Ticket
from django.db.models import Count

def home(request):
    locations = Location.objects.annotate(Count('ticket')).order_by('-ticket__count')[:20]
    return render(request, 'index.html', {'locations': locations})

def locationdetail(request, slug):
    loc = Location.objects.get(location_slug=slug)
    tickets = Ticket.objects.filter(location=loc).order_by('-date')
    return render(request, 'locationdetail.html', {'loc': loc, 'tickets': tickets})


