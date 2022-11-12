from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'account/templates/account/index.html')

def registro(request):
    pass

