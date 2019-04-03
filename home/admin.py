from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Trackers

class TrackersAdmin(ImportExportModelAdmin):
    list_display = ('group_name', 'safari_location', 'safari_start', 'safari_end', 'safari_days', 'agent', 'car_no', 'driver', 'start_endpoint', 'updated')
    list_display_links = ('group_name', 'safari_location')
    list_filter = ('agent','driver','car_no','file_handler')
    search_fields = ('group_name', 'safari_location', 'safari_start', 'safari_end', 'safari_days', 'agent', 'car_no', 'driver', 'start_endpoint', 'updated')
    list_per_page = 25
    date_hierarchy = ('updated')
    pass
    
admin.site.register(Trackers, TrackersAdmin) 