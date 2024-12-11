from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def movie (request):
    return HttpResponse ('<h1>pizza is acted by vjs</h1>') 
def thrillermovie (request):
    return HttpResponse ('<h1>DD returns is acted by santhanam</h1>')