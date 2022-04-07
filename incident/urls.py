
from django.urls import path

from incident.views import IncidentListView, IncidentDetailView 

urlpatterns = [
    path('', IncidentListView.as_view(), name='incident_list'),
    path('<slug:pk>', IncidentDetailView.as_view(), name='incident_details'),
]