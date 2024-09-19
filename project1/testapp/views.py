from django.shortcuts import render
from django.http import HttpResponse

def show(r):
    return HttpResponse('<h2>show template </h2>')