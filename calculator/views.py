from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .forms import ContactForm
from numpy import load, zeros, nan
from prediction_formula import *

def post_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            time1 = form.cleaned_data['time1']
            distance1 = int(form.cleaned_data['distance1'])
            time2 = form.cleaned_data['time2']
            distance2 = int(form.cleaned_data['distance2'])
            time3 = form.cleaned_data['time3']
            distance3 = int(form.cleaned_data['distance3'])
            distanceToPredict = form.cleaned_data['distanceToPredict']
            x = load('male.npy')
            data = nan*zeros(10)
            data[distance1] = time1
            data[distance2] = time2
            data[distance3] = time3
            tbc = zeros(10)
            tbc[distanceToPredict] = 1
            prediction = portal_to_prediction(x,data,tbc)
            html = "<html><body>Predicted time: %s.</body></html>" % convert_to_time(prediction)
            return HttpResponse(html)
    else:
        form = ContactForm()
        return render(request, 'calculator/post_edit.html', {'form': form})
