from django.shortcuts import render
from django.http import HttpResponse

def show(r):
    return HttpResponse('<h1>From testapp2<\h1>')
