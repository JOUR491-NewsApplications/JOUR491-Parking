from django.shortcuts import render
from django.http import HttpResponse
from tickets.models import Location, Reason, Ticket
from django.db.models import Count
from django.db import connection
import dateutil.parser

'''
def weekdaycount(locid):
    cursor = connection.cursor()
    cursor.execute("SELECT strftime('%w', date) as dayofweek, COUNT(*) as weekdaycount FROM tickets_ticket WHERE location_id=%i GROUP BY dayofweek") % locid
    row = cursor.fetchone()
    return row
'''

def home(request):
    locations = Location.objects.annotate(Count('ticket')).order_by('-ticket__count')[:20]
    return render(request, 'index.html', {'locations': locations})

def locationdetail(request, slug):
    loc = Location.objects.get(location_slug=slug)
    tickets = Ticket.objects.filter(location=loc).order_by('-date')
    total = tickets.count()
    truncate_date = connection.ops.date_trunc_sql('month','date')
    qs = tickets.extra({'month':truncate_date})
    months = qs.values('month').order_by('month').annotate(Count('date'))
    # Loop over month values with enumerate so we get an index value.
    for i, month in enumerate(months):
        # Modify each month in place. Parse out the date, which should totally sort of work.
        months[i]['month'] = dateutil.parser.parse(month['month'])
    return render(request, 'locationdetail.html', {'loc': loc, 'tickets': tickets, 'months': months, 'total': total,})


