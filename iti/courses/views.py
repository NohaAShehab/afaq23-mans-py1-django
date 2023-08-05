from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


courses = [
    {"id": 1, 'name': "python", "grade": 100},
    {"id": 2, 'name': "postgres", "grade": 100},
    {"id": 3, 'name': "django", "grade": 100}

]


def courses_index(request):
    return HttpResponse(courses)


def get_course(request, course_id):
    ## return with http response --> course details
    # for course in courses:
    #     if course["id"] ==  course_id:
    #         return HttpResponse(course.values())
    course = filter(lambda x: x['id']==course_id, courses)
    course = list(course)
    print(course)
    if course:
        return HttpResponse(course[0].values())

    return  HttpResponse("course not found ")

