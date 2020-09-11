from django.shortcuts import render, redirect
from . import models

def index(req):
    if req.POST:
        models.stokkopi.objects.create(name=req.POST['namaobat'], 
        jenisobat=req.POST['jenisobat'], quantity=req.POST['quantity'])
        return redirect('/stokkopi')

    tasks = models.Stokkopi.objects.all()
    return render(req, 'stokkopi/index.html',{
        'data': tasks,
    })


def detail(req, id):
    task = models.Stokkopi.objects.filter(pk=id).first()
    return render(req, 'stokkopi/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Stokkopi.objects.filter(pk=id).delete()
    return redirect('/stokkopi')

def update(req, id):
    if req.POST:
        task = models.Stokkopi.objects.filter(pk=id).update(name=req.POST['namaobat'], 
        jenisobat=req.POST['jenisobat'], quantity=req.POST['quantity'])
        return redirect('/stokkopi')

    task = models.Stokkopi.objects.filter(pk=id).first()
    return render(req, 'stokkopi/update.html', {
        'data': task,
    })
