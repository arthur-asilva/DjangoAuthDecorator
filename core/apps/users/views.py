from django.shortcuts import render, HttpResponse

def LoginView(request):
    return HttpResponse("First view to routers test")