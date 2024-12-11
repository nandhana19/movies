from django.urls import path
from horror.views import *
urlpatterns=[
    path('devil/',devil,name='devil'),
    path('maya/',maya,name='maya'),
]