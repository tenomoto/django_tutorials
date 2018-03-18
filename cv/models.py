from django.db import models

class Entry(models.Model):
    date_join = models.DateField()
    date_leave = models.DateField(null=True, blank=True)
    institution = models.CharField(max_length=200)
    position = models.CharField(max_length=200)