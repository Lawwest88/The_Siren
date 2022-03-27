from django.contrib import admin
from reporter.models import ReporterListView

class ReporterAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age')

admin.site.register(ReporterListView, ReporterAdmin)
