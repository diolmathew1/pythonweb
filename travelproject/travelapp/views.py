from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from travelapp.models import place,team

def demo(request):
    obj=place.objects.all()
    obj2=team.objects.all()

    return render(request,"index.html",{'places':obj,'teams':obj2})

