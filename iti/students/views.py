from django.shortcuts import render
from  django.http import  HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from students.models import Student


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


students = [
        {"id":1, "name":"Ahmed", 'image':'pic1.png'},
        {"id": 2, "name": "Ali", 'image': 'pic2.png'},
        {"id": 3, "name": "Mohamed", 'image': 'pic3.png'},
        {"id": 4, "name": "Mostafa", 'image': 'pic4.png'},
        {"id": 5, "name": "Omar", 'image': 'pic5.png'}
    ]

def index(request):


    allstudents = Student.objects.all()
    print(allstudents)
    # <QuerySet
    # consists of student objects
    # [<Student: Test_updated>, <Student: ddded>, <Student: Ali_updated>, <Student: abccc>]>
    return render(request, 'students/index.html',context={"students":allstudents})



def show(request,id):
    # student = filter(lambda std:std["id"]==id, students)
    # student = list(student)
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    # if student:
        # return HttpResponse(student[0])
    return  render(request, 'students/show.html', context={"student":student})


def delete(request, id):
    student = get_object_or_404(Student, id=id)  # object from student model
    student.delete()  # delete object from the database
    # return HttpResponse("deleted")
    return redirect('students.index')

