from django.shortcuts import render, redirect

from . import models

def index(req):
  barangs = models.Barang.objects.all()
  return render(req, 'barang/index.html', {
    'data': barangs,
  })

def create(req):
  if req.POST:
    models.Barang.objects.create(
      nama=req.POST['nama'],
      harga=req.POST['harga']
    )
    return redirect('/barang')

  return render(req, 'barang/create.html')

def update(req, id):
  if req.POST:
    models.Barang.objects.filter(pk=id).update(
      nama=req.POST['nama'],
      harga=req.POST['harga']
    )
    return redirect('/barang')

  barang = models.Barang.objects.filter(pk=id).first()
  return render(req, 'barang/update.html', {
    'data': barang,
  })

def delete(req, id):
  models.Barang.objects.filter(pk=id).delete()
  return redirect('/barang')
