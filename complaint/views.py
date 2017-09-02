from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request, 'registration.html', {})

def index2(request):
	return HttpResponse("<h1> This is Main complaint page  </h1>")