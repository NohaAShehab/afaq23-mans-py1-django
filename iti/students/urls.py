from django.contrib import admin
from django.urls import include, path

"""
    path(url, viewname(functionname))
    path('mywelcome', welcome)
"""
from django.contrib import admin
from django.urls import include, path
from students.views import index, show, delete, createStudent, editStudent
urlpatterns = [
    path('', index, name='students.index'),
    path('<int:id>', show, name='students.show'),
    path('<int:id>/delete',delete , name='students.delete' ),
    path('create',createStudent, name='students.create' ),
    path('<int:id>/edit',editStudent, name='students.edit' )
]