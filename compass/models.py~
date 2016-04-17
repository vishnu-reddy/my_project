from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Enquiry(models.Model):

    land_freight_management = "Land Freight Management"
    sea_freight_management = "Sea Freight Management"
    air_freight_management = "Air Freight Management"
    customs_clearance = "Customs Clearance"
    worldwide_door_delivery = "Worldwide Door Delivery"
    project_cargo_handling = "Project Cargo Handling"
    marine_insurance = "Marine Insurance"
    enquiry_choices = ((land_freight_management, 'Land Freight Management'),
     (sea_freight_management, "Sea Freight Management"),
    (air_freight_management, "Air Freight Management"),
     (customs_clearance , "Customs Clearance"),
     (worldwide_door_delivery , "Worldwide Door Delivery"),
     (project_cargo_handling , "Project Cargo Handling"),
     (marine_insurance , "Marine Insurance"))
    
    uae = "UAE"
    saudi_arabic = "Saudi Arabic"
    oman = "Oman"
    qatar = "Qatar"
    bahrain = "Bahrain"
    country_choices = ((uae, "UAE"),
	(saudi_arabic , "Saudi Arabic"),
	(oman, "Oman"),
	(qatar, "Qatar"),
	(bahrain, "Bahrain"))


    services = models.CharField(max_length=40, choices=enquiry_choices)
    full_name = models.CharField(max_length=30)
    organisation = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    contact_number = models.CharField(max_length=55)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=40, choices=country_choices)
    enquiry = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.full_name

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['services', 'full_name', 'organisation', 'designation', 'contact_number', 'email', 'city', 'country', 'enquiry']


class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.IntegerField()
    comment = models.TextField()


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
   def __unicode__(self):
        return self.reference_no
