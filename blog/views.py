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



# def atena_function(request, feeling):
#     txt = ""
#     # for _ in range(2):
#     for i in range(10):
#         txt += i * "\t"
#         txt += "I Love you Atena\n"
#     return HttpResponse(txt, content_type="text/plain")
#     # return HttpResponse(100 * "\tI Love you Atena\n", content_type="text/plain")
