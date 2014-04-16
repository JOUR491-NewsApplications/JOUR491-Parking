from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=255)
    location_slug = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/locations/%s/" % self.location_slug
    def __unicode__(self):
        return self.location

class Reason(models.Model):			
    reason = models.CharField(max_length=255)
    reason_slug = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/reasons/%s/" % self.reason_slug
    def __unicode__(self):
        return self.reason
	
class Ticket(models.Model):
    date = models.DateField()
    location = models.ForeignKey(Location)
    reason = models.ForeignKey(Reason)
    def get_absolute_url(self):
        return "/tickets/%i/" % self.id
    def __unicode__(self):
        return "A ticket on %s at %s" % (self.date, self.location)

