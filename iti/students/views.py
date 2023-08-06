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



def index(request):
    students = [
        {"id":1, "name":"Ahmed", 'image':'pic1.png'},
        {"id": 2, "name": "Ali", 'image': 'pic2.png'},
        {"id": 3, "name": "Mohamed", 'image': 'pic3.png'},
        {"id": 4, "name": "Mostafa", 'image': 'pic4.png'},
        {"id": 5, "name": "Omar", 'image': 'pic5.png'}
    ]

    return render(request, 'students/index.html',context={"students":students})

