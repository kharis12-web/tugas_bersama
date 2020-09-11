
from django.shortcuts import render, redirect
from . import models

def index(req):
    if req.POST:
        models.Karyawan.objects.create(name=req.POST['namaobat'], 
        jenisobat=req.POST['jenisobat'], quantity=req.POST['quantity'],
        alamat=req.POST['alamat'] )
        return redirect('karyawan')

    tasks = models.Karyawan.objects.all()
    return render(req, 'karyawan/index.html',{
        'data': tasks,
    })


def detail(req, id):
    task = models.Karyawan.objects.filter(pk=id).first()
    return render(req, 'datakaryawan/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Karyawan.objects.filter(pk=id).delete()
    return redirect('/datakaryawan')

def update(req, id):
    if req.POST:
        task = models.Karyawan.objects.filter(pk=id).update(name=req.POST['namaobat'], 
        jenisobat=req.POST['jenisobat'], quantity=req.POST['quantity'], 
        alamat=req.POST['alamat'])
        return redirect('/datakaryawan')

    task = models.Karyawan.objects.filter(pk=id).first()
    return render(req, 'karyawan/update.html', {
        'data': task,
    })
