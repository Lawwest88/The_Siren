from django.db import models

class ReporterListView(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    User_email  = models.EmailField(max_length=70,blank=True,unique=True)
    age = models.IntegerField(null=True)

