from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Enquiry(models.Model):

    vessel_agency = "Vessel Agency"
    customs_clearance = "Customs Clearance"
    trasportation = "Transportation"
    freight_forwarding = "Freight Forwarding"
    ship_chandling = "Ship Chandling"
    p_i_correspondents = "P & I Correspondents"
    enquiry_choices = ((vessel_agency, 'Vessel Agency'),
     (customs_clearance , "Customs Clearance"),
    (trasportation , "Transportation"),
     (freight_forwarding , "Freight Forwarding"),
     (ship_chandling , "Ship Chandling"),
     (p_i_correspondents , "P & I Correspondents"))
    
   
    services = models.CharField(max_length=40, choices=enquiry_choices)
    full_name = models.CharField(max_length=30)
    organisation = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    contact_number = models.CharField(max_length=55)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=80)
    enquiry = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.full_name

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['services', 'full_name', 'organisation', 'designation', 'contact_number', 'email', 'city', 'country', 'enquiry']


class Message(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

class Track(models.Model):
	
   dispatched = "Dispatched"
   pending = "Pending"
   out_of_delivery = "Out of Delivery"
   delivered = "Delivered"
   track_choices=((dispatched, "Dispatched"),
		(pending, "Pending"),
		(out_of_delivery,"Out of Delivery"),
		(delivered, "Delivered"))
   reference_no = models.CharField(max_length=100)
   from_location = models.CharField(max_length=40)
   to_location = models.CharField(max_length=40)
   type = models.CharField(max_length=40)
   date = models.DateField()
   status = models.CharField(max_length=40, choices=track_choices)
   no_of_pieces = models.IntegerField(null=True, blank=True)
   def __unicode__(self):
	
        return self.reference_no
class CurrentStatus(models.Model):
    dispatched = "Dispatched"
    pending = "Pending"
    out_of_delivery = "Out of Delivery"
    delivered = "Delivered"
    track_choices=((dispatched, "Dispatched"),
		(pending, "Pending"),
		(out_of_delivery,"Out of Delivery"),
		(delivered, "Delivered"))

    reference_no = models.ForeignKey(Track)
    currernt_date = models.DateField()
    current_from_location = models.CharField(max_length=100)
    current_to_location = models.CharField(max_length=100)
    status = models.CharField(max_length=40, choices=track_choices)
    def __unicode__(self):
	return self.status
