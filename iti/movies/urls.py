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
from django.urls import include, path
from movies.views import  CreateMovie, ListMovies, MovieCreateGenric, MovieListGeneric, \
    MovieEditGeneric, MovieDeleteGeneric, MovieDetailsGeneric
urlpatterns = [
    # path('create', CreateMovie.as_view(), name='movie.create'),
    # path('', ListMovies.as_view(), name='movies.index'),
    path('create', MovieCreateGenric.as_view(), name='movie.create'),
    path('', MovieListGeneric.as_view(), name='movies.index'),
    path('<int:pk>/edit', MovieEditGeneric.as_view(), name='movies.edit'),
    path('<int:pk>/delete', MovieDeleteGeneric.as_view(), name='movies.delete'),
    path('<int:pk>', MovieDetailsGeneric.as_view(), name='movies.show')


              ]


"""
    resource/  ===>list all 
    resource/id ===> list specific object 
    resources/id/edit
    resource/id/delete
    resource/create


"""
