from django.contrib import admin
from django.urls import include, path

"""
    path(url, viewname(functionname))
    path('mywelcome', welcome)
"""
from django.contrib import admin
from django.urls import include, path
from students.views import index, show
urlpatterns = [
    path('', index, name='students.index'),
    path('<int:id>', show, name='students.show')
]