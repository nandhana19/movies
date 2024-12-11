from django.urls import path
from thriller.views import *
urlpatterns=[
     path('movie/',movie,name='movie'),
     path('thrillermovie/',thrillermovie,name='thrillermovie'),

    
]