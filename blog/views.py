from django.http import HttpResponse
from django.shortcuts import render


def view1(request):
    return HttpResponse("you are in view 1")


def show_year(request, input_year):
    return HttpResponse(f"You are in year {input_year}")


def show_name(request, input_name):
    return HttpResponse(f"Your name is {input_name}")


def view3(request):
    return HttpResponse("you are in view 3")
