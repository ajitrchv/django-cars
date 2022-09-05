from audioop import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render

def dchome(request):
    try:
        return HttpResponseRedirect(reverse('cars:home'))
    except:
        return render(request,'home.html')