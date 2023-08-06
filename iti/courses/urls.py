


from django.urls import path
from courses.views import  courses_index, get_course, index
urlpatterns = [

    path('list', courses_index),
    path('<int:course_id>',get_course ),
    path('', index)

]
