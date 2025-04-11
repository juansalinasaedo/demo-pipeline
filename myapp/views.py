from django.http import JsonResponse
from django.shortcuts import render

def ping(request):
    return JsonResponse({'ping': 'pong'})


# Create your views here.
