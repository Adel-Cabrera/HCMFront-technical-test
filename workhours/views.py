from django.shortcuts import render

from .models import Workhours

# Create your views here.


def index(request):
    workhours = Workhours.objects.all()

    context = {
        'workhours': workhours
    }

    return render(request, 'workhours/index.html', context)


def edit(request):
    return render(request, 'workhours/edit.html')
