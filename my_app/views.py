from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact page")

    