from django.db import models

class Incident_type(models.Model):
    fire = models.CharField(max_length=50)
    police = models.CharField(max_length=50)
    medical = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
