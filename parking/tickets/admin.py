from django.contrib import admin
from tickets.models import Location, Reason, Ticket

admin.site.register(Location)
admin.site.register(Reason)
admin.site.register(Ticket)
