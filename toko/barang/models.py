from django.db import models

class Barang(models.Model):
  nama=models.CharField(max_length=225)
  harga=models.IntegerField()
