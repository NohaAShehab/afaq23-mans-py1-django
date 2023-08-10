from django.urls import path

from topics.views import create, create_via_model, index, edit
urlpatterns = [

    path('create', create, name='topics.create'),
    path('modelcreate' , create_via_model, name='topics.modelcreate'),
    path('',index, name='topics.index' ),
    path('<int:id>/edit',edit, name='topics.edit' )

]
