# -*- coding: utf-8 -*

from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from safecar.models import Car
import json

@csrf_exempt
def home(request):
    context = {}
    if request.method == 'POST':

        # Login actions
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context['warn_error'] = True

        else:
            login(request, user)
            return redirect('dashboard')
    return render_to_response('web/home.html', context, context_instance=RequestContext(request))

@login_required
def dashboard(request):
    context = {}
    car = Car.objects.get(user=request.user)
    context['car'] = car
    return render_to_response('web/dashboard.html', context, context_instance=RequestContext(request))

@login_required
def map(request):
    context = {}
    return render_to_response('web/map.html', context, context_instance=RequestContext(request))

@login_required
def map_iframe(request):
    context = {}
    return render_to_response('web/map-iframe.html', context, context_instance=RequestContext(request))

@login_required
@csrf_exempt
def set_location(request):
    if request.method == 'POST' or request.method == 'GET':
        response_data = {}
        car = Car.objects.get(user=request.user)

        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)

        if (latitude, longitude) != (None, None):
            car.latitude = latitude
            car.longitude = longitude
            car.save()

        response_data['car'] = {}
        response_data['car']['latitude'] = car.latitude
        response_data['car']['longitude'] = car.longitude
        response_data['lat'] = car.latitude
        response_data['lng'] = car.longitude

        return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required
@csrf_exempt
def mark_status(request):
    if request.method == 'POST':
        response_data = {}
        car = Car.objects.get(user=request.user)

        action = request.POST['action']
        print action
        if action == 'lock':
            car.is_locked = True
        elif action == 'unlock':
            car.is_locked = False
        elif action == 'play_alarm':
            car.play_alarm = True
        elif action == 'unplay_alarm':
            car.play_alarm = False
        elif action == 'turnon':
            car.is_turnedon = True
        elif action == 'turnoff':
            car.is_turnedon = False

        car.save()
        response_data['car'] = {}
        response_data['car']['is_turnedon'] = car.is_turnedon
        response_data['car']['is_locked'] = car.is_locked
        response_data['car']['is_walking'] = car.is_walking
        response_data['car']['play_alarm'] = car.play_alarm

        return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def api_login(request):
    """
    Do login of the user

    **Context**

    None

    **Template:**

    None
    """
    response_data = {}
    if request.method == 'POST':
        response_data = {}

        # Login actions

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            response_data['result'] = 'fail'
            response_data['message'] = 'Login ou senha estão incorretos! Por favor, verifique.'
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            login(request, user)
            response_data['result'] = 'success'
            response_data['message'] = 'Login feito com sucesso!'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps(response_data), content_type="application/json")
