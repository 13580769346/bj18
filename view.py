from django.http import HttpResponse
import time

def index(request):
    return HttpResponse('ok')