from django.contrib import admin
from django.urls import include, path

"""
    path(url, viewname(functionname))
    path('mywelcome', welcome)
"""
from django.contrib import admin
from django.urls import include, path
from students.views import index
urlpatterns = [
    path('', index)
]