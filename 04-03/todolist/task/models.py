from django.db import models
class Task(models.Model):
	merk_coffe = models.TextField(default='')
	type_coffe = models.TextField(default='')
	roasteds = models.TextField(default='')
	process = models.TextField(default='')
	altitudes = models.TextField(default='')