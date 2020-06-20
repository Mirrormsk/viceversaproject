from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    return render(request, 'reverse.html', {'reverse': request['viceversa']})