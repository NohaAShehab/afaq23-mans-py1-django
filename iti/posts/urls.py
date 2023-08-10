from django.urls import path

from posts.views import index, create, delete, edit

urlpatterns = [

    path('', index, name='posts.index'),
    path('new',create, name='posts.new'),
    path('<int:id>/delete',delete, name='posts.delete' ),
    path('<int:id>/edit',edit, name='posts.edit' ),

]
