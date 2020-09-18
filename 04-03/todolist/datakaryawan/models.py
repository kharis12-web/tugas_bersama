from django.db import models

class Karyawan(models.Model):
    name = models.TextField(default='')
    jenisobat = models.TextField(default='')
    quantity = models.TextField(default='')
    alamat = models.TextField(default='')