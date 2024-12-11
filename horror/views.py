from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def devil (request):
    return HttpResponse ('<h1><marquee>this movie released in 2024</marquee></h1>') 
def maya (request):
    return HttpResponse('<h1><marquee>the lead actress is nayanthara</marquee></h1>')