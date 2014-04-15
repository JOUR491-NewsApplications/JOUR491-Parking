class Location(models.Model):
	location = models.Charfield(max_length=255)
	location_slug = models.Charfield(max_length=255)

class Reason(models.Model):			
	reason = models.Charfield(max_lenght=255)
	reason_slug = models.Charfield(max_length=255)
	
class Ticket(models.Model):
	datetime.date()
	location = models.ForeignKey(Loaction)
	reason = models.ForeignKey(Reason)

					