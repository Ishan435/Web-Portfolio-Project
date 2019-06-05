from django.shortcuts import render

# Create your views here.

from .models import Work

def home(request):

    jobs=Work.objects
    return render(request,'work/home.html',{"mywork":jobs})
