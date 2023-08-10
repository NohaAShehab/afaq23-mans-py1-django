from django.urls import path

from tracks.views import index, show

urlpatterns = [
    path('', index, name='tracks.index'),
    path('<int:id>', show, name='tracks.show')
]
