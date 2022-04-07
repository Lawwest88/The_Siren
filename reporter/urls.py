
from django.urls import path

from reporter.views import ReporterListView, ReporterDetailView

urlpatterns = [
    path('', ReporterListView.as_view(), name='reporter_list'),
    path('<slug:pk>', ReporterDetailView.as_view(), name='Reporter_details'),
]