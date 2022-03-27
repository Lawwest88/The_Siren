
from django.urls import path

from reporter.views import ReporterListView

urlpatterns = [
    path('', ReporterListView.as_view(), name='reporter_list'),
]