from django.shortcuts import render, HttpResponse, redirect
from ..log_reg.models import User
from .models import *
from django.contrib import messages

def index(request):
    context = {
        'trips' : Trip.objects.filter(trip_members=request.session['user_id']),
        'other_trips' : Trip.objects.exclude(trip_members=request.session['user_id'])
    }
    return render(request, "belt_app/travels.html", context)

def destination(request, id):
    context = {
        'trip' : Trip.objects.get(id=id),
        'planner' : User.objects.get(id=(Trip.objects.get(id=id).created_by_id)).name,
        'others' : User.objects.filter(joined_trips=id).exclude(id=(Trip.objects.get(id=id).created_by_id))
    }
    return render(request, "belt_app/destination.html", context)

def add(request):

    return render(request, "belt_app/add.html")

def processTrip(request):
    response = Trip.objects.trip_validator(request.POST)
    print(request.POST['date_from'])
    if response['status'] == False:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/travels/add', messages)    
    else:
        return redirect('/travels')

def join(request, id):
    trip = Trip.objects.get(id=id)
    trip.trip_members.add(User.objects.get(id=request.session['user_id']))
    return redirect('/travels')