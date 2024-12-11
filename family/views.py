from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def movie (request):
    return HttpResponse ('<h1>yaanai was family movie</h1>') 
