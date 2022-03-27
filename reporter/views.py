from django.views.generic import ListView
from reporter.models import ReporterListView


class ReporterListView(ListView):
    model = ReporterListView
    # paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['now'] = timezone.now()
    #    return context
