from django.http import HttpResponse
from django.shortcuts import render

def short_redirect_view(request, *args, **kwargs):
	return HttpResponse("Hello Gert!")
