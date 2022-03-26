from django.contrib import admin
from reporter.models import Reporter

class ReporterAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age')

admin.site.register(Reporter, ReporterAdmin)
