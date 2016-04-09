from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .forms import PerformanceForm 
from numpy import load, zeros, nan
from prediction_formula import *
from getpass import getuser

USER = getuser()

def enter_perform(request):
    if request.method == "POST":
        form = PerformanceForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            distance1 = int(form.cleaned_data['distance1'])
            time1 = convert_to_seconds(form.cleaned_data['time1'])
            try:
                distance2 = int(form.cleaned_data['distance2'])
                time2 = convert_to_seconds(form.cleaned_data['time2'])
            except ValueError:
                distance2 = np.nan
            try:
                distance3 = int(form.cleaned_data['distance3'])
                time3 = convert_to_seconds(form.cleaned_data['time3'])
            except ValueError:
                distance3 = np.nan
            distanceToPredict = form.cleaned_data['distanceToPredict']
            if USER=='duncanblythe':
                if gender=='M':
                    x = load('male.npy')
                else:
                    x = load('female.npy')
            else:
                if gender=='M':
                    x = load('/home/blythed/running_calculator/male.npy')
                else:
                    x = load('/home/blythed/running_calculator/female.npy')
            data = nan*zeros(10)
            data[distance1] = time1
            if not(np.isnan(distance2)):
                data[distance2] = time2
            if not(np.isnan(distance3)):
                data[distance3] = time3
            tbc = zeros(10)
            tbc[distanceToPredict] = 1
            prediction = portal_to_prediction(x,data,tbc)
            #html = "<html><body>Predicted time: %s</body></html>" % convert_to_time(prediction)
            #return HttpResponse(html)
            #form = PerformanceForm()
            return render(request, 'calculator/enter_times.html', {'form':form, 'results': 'Prediction: '+convert_to_time(prediction)})
    else:
        form = PerformanceForm()
        return render(request, 'calculator/enter_times.html', {'form': form, 'results': 'Prediction: '})
