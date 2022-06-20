from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def userlist(request):
    return HttpResponse('hello, Welcome to our online profiler list!!!')
