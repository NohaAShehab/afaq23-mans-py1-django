


from django.urls import path
from courses.views import  courses_index, get_course
urlpatterns = [

    path('index', courses_index),
    path('<int:course_id>',get_course )

]
