from ast import Return
from multiprocessing import context
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


# Create your views here.



def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}
    return render(request,'cars/list.html', context=context)

def add(request):
    
    #---------- Posting data to db
    
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request,'cars/add.html')
    #---------------------------------------------------
    
    
    

def delete(request):
    
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}
    if request.POST:
        #,mjhb
        pk =request.POST['key']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print("KEY not found!")
            return redirect(reverse('cars:list'))
            
    else:
        return render(request,'cars/delete.html', context=context)


def home(request):
    return render(request,'cars/home.html')

