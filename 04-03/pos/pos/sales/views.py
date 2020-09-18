from django.shortcuts import render,redirect

from customers import models as customers_models
# from product import models as product_models
from . import models, forms
# Create your views here.
def index(req):

	sale = models.Sale.objects.all()
	return render(req, ('sales/index.html'), {
		'data' : sale,
		})

def input(req):
	form = forms.Sale()

	if req.POST:
		form = forms.Sale(req.POST)
		if form.is_valid():
			form.save()
		return redirect('/sales')

	sale = models.Sale.objects.all()
	return render(req, ('sales/input.html'), {
		'data' : sale,
		'form' : form,
		})

def update(req, id):
	if req.POST:
		form = forms.Sale(req.POST)
		if form.is_valid():
			form.save()
		return redirect('/sales')

	sale = models.Sale.objects.all()
	return render(req, ('sales/input.html'), {
		'data' : sale,
		'form' : form,
		})

def print(req):
	print = models.Sale.objects.all()
	return render(req, ('sales/print.html'), {
		'data' : print,
		})
	
def delete(req, id):
	models.Sale.objects.filter(pk=id).delete()
	return redirect('/sales')
