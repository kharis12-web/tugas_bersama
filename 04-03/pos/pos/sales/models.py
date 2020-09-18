from django.db import models
from datetime import datetime
from customers import models as customers_models
from products import models as products_models
# Create your models here.
class Sale(models.Model):
	date = models.DateField(default=datetime.now)
	cust = models.ForeignKey(customers_models.Cust, on_delete=models.CASCADE, related_name='membeli')
	products = models.ForeignKey(products_models.Prod, on_delete=models.CASCADE, related_name='terjual')
	qty = models.IntegerField(default='')

	def __str__(self):
		return self.products, self.date, self.qty, self.cust

	def total(self):
		return self.qty*self.products.price

class Print(models.Model):
	print = models.ForeignKey(Sale, on_delete=models.CASCADE)