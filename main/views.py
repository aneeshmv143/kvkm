from django.shortcuts import *
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import *

def index(request):
	response = {}

	return render_to_response('index.html', response, context_instance=RequestContext(request))