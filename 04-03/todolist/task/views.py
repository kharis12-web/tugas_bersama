from django.shortcuts import render, redirect
from . import models

def index(req):
    if req.POST:
        models.Task.objects.create(
            merk_coffe=req.POST['merk_coffe'],
            type_coffe=req.POST['type_coffe'],
            roasteds=req.POST['roasteds'],
            process=req.POST['process'],
            altitudes=req.POST['altitudes'])
        return redirect('/task')

    tasks = models.Task.objects.all()
    return render(req, 'task/index.html',{
        'data': tasks,
    })


def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/task')

def update(req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(
            merk_coffe=req.POST['merk_coffe'],
            type_coffe=req.POST['type_coffe'],
            roasteds=req.POST['roasteds'],
            process=req.POST['process'],
            altitudes=req.POST['altitudes'])
        return redirect('/task')

    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/update.html', {
        'data': task,
    })
