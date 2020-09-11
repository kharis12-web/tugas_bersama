from django.db import models

class Alat(models.Model):
    name = models.TextField(default='')
    jenisobat = models.TextField(default='')
    quantity = models.TextField(default='')
  
