from django.db import models

# Create your models here.
class Buy(models.Model):
	name = models.TextField(default='')
	brg = models.TextField(default='')
	jmlh = models.TextField(default='')
	# price = models.TextField(default='')