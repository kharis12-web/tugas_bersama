from django.db import models
class Suplayer(models.Model):
    name = models.TextField(default='')
    jenisobat = models.TextField(default='')
    quantity = models.TextField(default='')
  
