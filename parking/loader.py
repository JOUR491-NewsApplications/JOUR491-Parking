import os, sys, string, csv, datetime, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parking.settings") 

from tickets.models import Location, Reason, Ticket

from django.template.defaultfilters import slugify, urlize
from django.core.exceptions import ObjectDoesNotExist

reader = csv.reader(open("tickets.csv", "rU"), dialect=csv.excel)
reader.next()
for row in reader:
    try:
        cite = row[0]
        loc = row[2]
        loc_slug = slugify(row[2])
        locat, locatcreated = Location.objects.get_or_create(location=loc, location_slug=loc_slug)
        rea = row[3]
        rea_slug = slugify(row[3])
        reas, reascreated = Reason.objects.get_or_create(reason=rea, reason_slug=rea_slug)
        tickparse = time.strptime(row[1], "%m/%d/%y %H:%M %p")
        tick_date = datetime.datetime(tickparse.tm_year, tickparse.tm_mon, tickparse.tm_mday, tickparse.tm_hour, tickparse.tm_min)
        tick, tickcreated = Ticket.objects.get_or_create(citation_number=cite, date=tick_date, location=locat, reason=reas)
        print tickcreated
    except:
        print "BOOOOOOOORRRRRRK!"
    




#        if row[1] == "P":
#            if row[30] == "G":
#                at = "Grant"
#                ats = "grant"
#            awt, awtcreated = AwardType.objects.get_or_create(award_type=at, award_type_slug=ats)
#            funda = row[11]
#            funda_slug = slugify(funda[0:50])
#            ag, agcreated = Agency.objects.get_or_create(agency_name=funda, agency_name_slug=funda_slug)
#            aid = row[0]
#            aw_date_year = int(row[31][0:4])
#            aw_date_month = int(row[31][5:7])
#            aw_date_day = int(row[31][8:10])
#            aw_date = datetime.datetime(aw_date_year, aw_date_month, aw_date_day)
#            rname = row[18]
#            rstate = row[20]
#            rzip = row[19]
#            awid = row[21]
#            adesc = row[32]
#            try:
#                amt = float(row[33])
#            except:
#                amt = None
#            try:
#                amtd = float(row[40])
#            except:
#                amtd = None
#            try:
#                numjobs = float(row[38])
#            except:
#                numjobs = None
#            jcdesc = row[37]
#            try:
#                aw = PrimaryAward.objects.get(arra_id=aid)
#                aw.arra_id=aid
#                aw.award_type=awt
#                aw.awarding_agency=ag
#                aw.award_date=aw_date
#                aw.recipient_name=rname
#                aw.recipient_state=rstate
#                aw.recipient_zipcode=rzip
#                aw.award_id=awid
#                aw.award_description=adesc
#                aw.amount_awarded=amt
#                aw.amount_disbursed=amtd
#                aw.reported_number_of_jobs_created=numjobs
#                aw.jobs_created_description=jcdesc
#                aw.save()
#                print "Updated %s" % aw
#            except:
#                aw, awcreated = PrimaryAward.objects.get_or_create(arra_id=aid, award_type=awt, awarding_agency=ag, award_date=aw_date, recipient_name=rname, recipient_state=rstate, recipient_zipcode=rzip, award_id=awid, award_description=adesc, amount_awarded=amt, amount_disbursed=amtd, reported_number_of_jobs_created=numjobs, jobs_created_description=jcdesc)
#                print "Created %s" % aw
#
#reader = csv.reader(open("All_GrantsY11Q1.csv"), dialect=csv.excel)
#reader.next()
#for row in reader:
#    if row[1] == "S":
#        if row[30] == "G":
#                akey = row[0]
#                at = "Grant"
#                ats = "grant"
#                awt = AwardType.objects.get(id=1)
#                funda = row[11]
#                funda_slug = slugify(funda[0:50])
#                ag = Agency.objects.get(agency_name=funda, agency_name_slug=funda_slug)
#                try:
#                    aw_date_year = int(row[31][0:4])
#                    aw_date_month = int(row[31][5:7])
#                    aw_date_day = int(row[31][8:10])
#                    aw_date = datetime.datetime(aw_date_year, aw_date_month, aw_date_day)
#                except:
#                    continue
#                rduns = row[17]
#                rname = row[18]
#                rstate = row[20]
#                rzip = row[19]
#                awid = row[21]
#                sawid = row[23]
#                adesc = row[32]
#                try:
#                    amt = float(row[34])
#                except:
#                    amt = None
#                try:
#                    amtd = float(row[41])
#                except:
#                    amtd = float(0)
#                try:
#                    numjobs = float(row[38])
#                except:
#                    numjobs = None
#                jcdesc = row[37]
#                try:
#                    aw = PrimaryAward.objects.get(award_id=awid)
#                    try:
#                        sw = SecondaryAward.objects.get(award_id=sawid, award_key=akey, primary_award=aw)
#                        sw.award_description=adesc
#                        sw.amount_awarded=amt
#                        sw.amount_disbursed=amtd
#                        sw.reported_number_of_jobs_created=numjobs
#                        sw.jobs_created_description=jcdesc
#                        sw.save()
#                        print "Updated %s" % sw
#                    except:
#                        sw, swcreated = SecondaryAward.objects.get_or_create(primary_award=aw, award_type=awt, awarding_agency=ag, award_date=aw_date, recipient_name=rname, recipient_state=rstate, recipient_zipcode=rzip, award_id=sawid, award_description=adesc, amount_awarded=amt, amount_disbursed=amtd, reported_number_of_jobs_created=numjobs, jobs_created_description=jcdesc, award_key=akey)
#                        print "Created %s" % sw
#                except:
#                    continue

#To just update what's in place, use these.

# Update the existing Primary Awards
