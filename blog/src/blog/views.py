from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello")

def index_id(request, id):
    return HttpResponse("Hello")

def index_title(request, title):
    return HttpResponse("Hello Title")

# def first(request):
#     return render(request, "index.html")

def first(request):
    context_dict = {
        "name": "Elissa"
    }
    return render(request, "index.html", context_dict)

def second(request):
    # return redirect("https://google.com")
    # return redirect("/first")
    # return redirect("first")
    # return redirect("index_id", id=5)
    return redirect("index_title", title="cr7")

def third(request):
    return JsonResponse({"id": 123, "name": "Elissa"})