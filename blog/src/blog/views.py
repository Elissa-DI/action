from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello")

def index_id(request, id):
    return HttpResponse("Hello")

def index_title(request, title):
    return HttpResponse("Hello Title")