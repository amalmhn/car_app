from django.shortcuts import render, redirect
from .forms import CarCreateForm
from .models import Car

# Create your views here.

#CreateCar
'''get>html page with form
    post>save to the model'''
def car_create(request):
    form = CarCreateForm()
    context = {}
    context['form'] = form
    car = Car.objects.all()
    context['car']=car
    if (request.method=='POST'):
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            form = CarCreateForm(request.POST)
            car = Car.objects.all()
            context = {}
            context['form'] = form
            context['car'] = car
            return render(request,'carapp/createCar.html',context)

    return render(request,'carapp/createCar.html',context)

#view
'''get>html page with the details of the car in table'''
def view_car(request,id):
    car = Car.objects.get(id=id)
    context = {}
    context['car'] = car
    return render(request,'carapp/viewCar.html',context)

#edit
'''get>an html page with form with details and a edit button
    post>after edit you need to click the button and post the details to edit in the model'''
def edit_car(request,id):
    car = Car.objects.get(id=id)
    context = {}
    context['car'] = car
    form = CarCreateForm(instance=car)
    context['form'] = form
    if request.method=='POST':
        form = CarCreateForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            form = CarCreateForm(request.POST,instance=car)
            context = {}
            context['form'] = form
            return render(request,'carapp/editCar.html',context)
    return render(request,'carapp/editCar.html',context)

#delete
'''get>when you click delete the car should delete from table and load to the same page'''
def delete_car(request,id):
    Car.objects.get(id=id).delete()
    return redirect('create')