# -*- coding: utf-8 -*

from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

def home(request):
	context = {}
	return render_to_response('web/home.html', context, context_instance=RequestContext(request))

def dashboard(request):
	context = {}
	return render_to_response('web/dashboard.html', context, context_instance=RequestContext(request))

def map(request):
	context = {}
	return render_to_response('web/map.html', context, context_instance=RequestContext(request))