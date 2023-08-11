from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import  CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from django.http import HttpResponse

from movies.models import Movie
from movies.forms import  MovieForm
# Create your views here.


## class based views --->

# view  .===> create new movie ?

class CreateMovie(View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'movies/create.html', context={'form':form})
    def post(self, request):
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse('saved')
            return  redirect('movies.index')

        return render(request, 'movies/create.html',context={'form':form} )



class ListMovies(View):
    def get(self, request):
        movies = Movie.get_all_objects()
        return render(request, 'movies/index.html', context={"movies": movies})


class MovieCreateGenric(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = '/movies/'
    template_name = 'movies/create.html'

class MovieListGeneric(ListView):
    model = Movie
    template_name = 'movies/index.html'
    ## you catch the returned object with key : objects
    context_object_name = 'movies'

class MovieEditGeneric(UpdateView):
    model = Movie
    template_name = 'movies/edit.html'
    success_url = '/movies/'
    form_class = MovieForm



class MovieDeleteGeneric(DeleteView):
    model = Movie
    success_url = '/movies/'
    template_name = 'movies/delete.html'


class MovieDetailsGeneric(DetailView):
    model = Movie
    template_name = 'movies/show.html'
    context_object_name = 'movie'