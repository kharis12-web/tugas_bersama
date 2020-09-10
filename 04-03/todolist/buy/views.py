from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(req):
	buy = models.Buy.objects.all()
	return render(req, 'buy/index.html', {
		'data' : buy,
		})
def input(req):
	if req.POST:
		models.Buy.objects.create(
			name=req.POST['name'],
			brg=req.POST['brg'],
			jmlh=req.POST['jmlh'],
			price=req.POST['price'])
		return redirect('/buy')

	buy = models.Buy.objects.all()
	return render(req, 'buy/input.html', {
		'data' : buy,
		})