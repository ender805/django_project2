from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
        if request.method == "GET":
         return HttpResponse("This was a GET request  it was just Hello, Maciej")
        elif request.method == "POST":
         return HttpResponse("This was a POST request")