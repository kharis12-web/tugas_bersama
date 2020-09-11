from django.db import models
class Stokkopi(models.Model):
    name = models.TextField(default='')
    jenisobat = models.TextField(default='')
    quantity = models.TextField(default='')