from django.views.generic import ListView, DetailView
from reporter.models import ReporterListView, Reporter



class ReporterListView(ListView):
    model = ReporterListView
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReporterListView(DetailView):
    model = Reporter
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context