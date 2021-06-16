from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    return render(request, 'main/index.html')


def today(request):
    return render(request, 'main/today.html')
