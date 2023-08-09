
from django.urls import include, path
from tracks.views import index, show
urlpatterns = [
    path('', index, name='tracks.index'),
    path('<int:id>',show, name='tracks.show')
]