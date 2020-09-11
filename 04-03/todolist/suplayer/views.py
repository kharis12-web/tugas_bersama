from django.shortcuts import render, redirect
from . import models

def index(req):
    if req.POST:
        models.Suplayer.objects.create(name=req.POST['namaobat'], 
        jenisobat=req.POST['jenisobat'], quantity=req.POST['quantity'])
        return redirect('/suplayer')

    tasks = models.Suplayer.objects.all()
    return render(req, 'suplayer/index.html',{
        'data': tasks,
    })


def detail(req, id):
    task = models.Suplayer.objects.filter(pk=id).first()
    return render(req, 'suplayer/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Suplayer.objects.filter(pk=id).delete()
    return redirect('/suplayer')

def update(req, id):
    if req.POST:
        task = models.Suplayer.objects.filter(pk=id).update(name=req.POST['namaobat'], 
        jenisobat=req.POST['jenisobat'], quantity=req.POST['quantity'])
        return redirect('/suplayer')

    task = models.Suplayer.objects.filter(pk=id).first()
    return render(req, 'suplayer/update.html', {
        'data': task,
    })
