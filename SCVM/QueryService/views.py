from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>BDSA Query Service</h1>')
# Create your views here.
