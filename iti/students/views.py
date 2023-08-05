from django.shortcuts import render
from  django.http import  HttpResponse
# Create your views here.


## views functions

## any views function must have request as the first parameter in the view,
# any view must return with http response
def helloworld(request):
    return HttpResponse("Hello world")


def welcome(request):
    return HttpResponse("<h1 style='color:red; text-align:center'>  Welcome </h1>")



def saywelcome(request, name):
    return HttpResponse(f"<h1 style='color:purple; text-align:center'>  Welcome {name} </h1>")



def sumnums(request, num1, num2):
    """ urls parameter are strings """

    return HttpResponse(f"<h1> num1 + num2 = {num1 + num2} </h1>")

