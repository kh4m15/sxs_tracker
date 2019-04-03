from django.db import models

from django.db import models
from datetime import datetime

class Trackers(models.Model):
    group_name = models.CharField(max_length=200)
    hotel_date_in = models.DateField()
    hotel_date_out = models.DateField()
    no_of_nights = models.IntegerField()
    safari_code = models.IntegerField()
    safari_location = models.CharField(max_length=200, blank=True)
    safari_start = models.DateField()
    safari_end = models.DateField()
    safari_days = models.IntegerField()
    booking_number = models.IntegerField(blank=True, null=True)
    booking_status = models.CharField(max_length=200)
    invoice_number = models.IntegerField()
    amount = models.IntegerField()
    paid_notpaid = models.CharField(max_length=200)
    tour_leader = models.CharField(max_length=200)
    week = models.IntegerField(blank=True, null=True)
    no_of_adults = models.IntegerField()
    no_of_children = models.IntegerField(blank=True,  null=True)
    arrival_flight = models.CharField(max_length=200)
    arrival_time = models.TimeField(blank=True, null=True)
    room_type = models.CharField(max_length=200)
    agent = models.CharField(max_length=200)
    sxs_consultant = models.CharField(max_length=200)
    depart_flight_number = models.CharField(max_length=200)
    depart_flight_time = models.TimeField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    file_handler = models.CharField(max_length=200)
    updated = models.DateTimeField(default=datetime.now, blank=True, null=True)
    comments = models.CharField(max_length=200)
    car_no = models.CharField(max_length=200, blank=True)
    driver = models.CharField(max_length=200)
    start_endpoint = models.CharField(max_length=200)
    def __str__(self):
        return self.group_name
    

