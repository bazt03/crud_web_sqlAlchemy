from django.contrib import messages
from django.db import models

#from django.http import JsonResponse
#from django.core import serializers

# Create your models here.
class Empleado(models.Model):
    emp_name = models.TextField()
    emp_emial = models.TextField()
    emp_mobile = models.TextField()
    emp_address = models.TextField()
    

    