from django.contrib import admin
from incident.models import Incident_type

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('fire','medical','police','created')

admin.site.register(Incident_type, IncidentAdmin)
