"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

"""
    path(url, viewname(functionname))
    path('mywelcome', welcome)
"""
from django.conf.urls.static import static
from django.conf import settings

from students.views import helloworld, welcome, saywelcome, sumnums

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('hello', helloworld),
                  path('mywelcome', welcome),
                  path("welcome/<name>", saywelcome),
                  ## restrict url parameters to be int
                  path('sum/<int:num1>/<int:num2>', sumnums),
                  # path('courses/index', courses_index)

                  # include urls in courses/urls.py --> any url in courses.urls --> called with prefix courses
                  path('courses/', include('courses.urls')),
                  path('students/', include('students.urls')),
                  path('tracks/', include('tracks.urls')),
                  path('posts/', include('posts.urls')),
                  path('topics/', include('topics.urls')),
                  path('movies/', include('movies.urls')),
                  path('accounts/', include('accounts.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
