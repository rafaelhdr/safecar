# -*- coding: utf-8 -*

from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

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
    return render_to_response('web/dashboard.html', context, context_instance=RequestContext(request))

@login_required
def map(request):
    context = {}
    return render_to_response('web/map.html', context, context_instance=RequestContext(request))