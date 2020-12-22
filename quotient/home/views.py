from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("This is home page!")


def about(request):
    return HttpResponse("This is about page")
