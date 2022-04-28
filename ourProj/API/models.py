from tabnanny import verbose
from django.db import models
 
class PDF(models.Model):
    namePDF = models.CharField("", max_length=50)
    base64 = models.CharField("", max_length=50)

class Report(models.Model):
    group = models.CharField("", max_length=20)
    labNumber = models.PositiveSmallIntegerField("", default=1)
    name = models.CharField("", max_length=100)
    points = models.PositiveSmallIntegerField("", default=0)
    githubURL = models.SlugField(max_length=150, unique=True)
    reportID = models.CharField("", max_length=150)
    pdf = models.ForeignKey(PDF, on_delete=models.PROTECT)
