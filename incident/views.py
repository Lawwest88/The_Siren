from django.views.generic import ListView, DetailView
from incident.models import Incident_type
from incident.models import Incident


class IncidentListView(ListView):
    model = Incident_type
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context


class IncidentListView(DetailView):
    model = Incident

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context