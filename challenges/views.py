from django.shortcuts import render
from django.http import HttpResponse


def january(request):
    return HttpResponse("Hello, world. You're at the challenges index1.")

def february(request):
    return HttpResponse("Hello, February. Walk 20 minutes every day.")