from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def logreg(request):
    
    return render(request, "log_reg/log_reg.html")

def processReg(request):
    response = User.objects.reg_validator(request.POST)
    if response['status'] == False:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/', messages)
    else:
        request.session['user_id'] = response['user_id']
        request.session['name'] = User.objects.get(id=response['user_id']).name
        return redirect('/success')

def processLog(request):
    response = User.objects.log_validator(request.POST)
    if response['status'] == False:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/', messages)
    else:
        request.session['user_id'] = response['user_id']
        request.session['name'] = User.objects.get(id=response['user_id']).name
        return redirect('/success')

def success(request):
    if 'user_id' in request.session:
        return redirect('/travels')
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')