
from django.urls import path

from incident.views import IncidentListView

urlpatterns = [
    path('', IncidentListView.as_view(), name='incident_list'),
]