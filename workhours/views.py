from django.shortcuts import render, redirect
from .models import Workhours
from .forms import *

# Create your views here.


def new(request):
    if request.method == "POST":
        form = WorkhourForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = WorkhourForm()
    return render(request, 'workhours/new.html', {'form': form})


def show(request):
    workhours = Workhours.objects.all()
    return render(request, "workhours/show.html", {'workhours': workhours})


def details(request, id):
    workhour = Workhours.objects.get(id=id)
    return render(request, 'workhours/details.html', {'workhour': workhour})


def edit(request, id):
    workhour = Workhours.objects.get(id=id)
    return render(request, 'workhours/edit.html', {'workhour': workhour})


def update(request, id):
    workhour = Workhours.objects.get(id=id)
    form = WorkhourForm(request.POST, instance=workhour)
    print(form.errors)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'workhours/edit.html', {'workhour': workhour})


def delete(request, id):
    workhour = Workhours.objects.get(id=id)
    workhour.delete()
    return redirect("/show")
