from django.db import models

# Create your models here.

class main_erp(models.Model):
    inspection_yes = models.CharField(max_length=1)
    inspection_no = models.CharField(max_length=1)
    Preventitive_yes = models.CharField(max_length=1)
    Preventitive_no = models.CharField(max_length=1)
    repairs_yes = models.CharField(max_length=1)
    repairs_no = models.CharField(max_length=1)
    current_yes = models.CharField(max_length=1)
    current_no = models.CharField(max_length=1)

class planning_erp(models.Model):
    response_yes = models.CharField(max_length=1)
    response_no = models.CharField(max_length=1)
    plan_yes = models.CharField(max_length=1)
    plan_no = models.CharField(max_length=1)
    integrated_yes = models.CharField(max_length=1)
    integrated_nos = models.CharField(max_length=1)
    current_yes = models.CharField(max_length=1)
    current_no = models.CharField(max_length=1)
    