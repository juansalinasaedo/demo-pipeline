from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render

def ping(request):
    return JsonResponse({'ping': 'pong', 'date': datetime.now().isoformat()})


# Create your views here.
