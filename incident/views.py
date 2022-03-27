from django.views.generic import ListView
from incident.models import Incident_type


class IncidentListView(ListView):
    model = Incident_type
    # paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['now'] = timezone.now()
    #    return context
