from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post


# Create your views here.


# list all

def index(request):
    posts = Post.get_all_objects()
    return render(request, 'posts/index.html', context={"posts": posts})
# create
def create(request):
    ## request
    """ when you use multi-part form data to upload file//
    you can find the file in ===> request.FILES"""
    if request.method== 'POST':
        print(request.POST)
        title = request.POST["title"]
        body = request.POST["body"]
        # print(request.FILES)
        image = request.FILES["image"]

        post = Post()
        post.title = title
        post.body = body
        post.image =image
        post.save()
        # return HttpResponse("New object")
        return redirect('posts.index')


    return render(request, 'posts/create.html')

## update
def edit(request, id):
    post = Post.get_specific_object(id)
    if request.method=='POST':
        title = request.POST["title"]
        body = request.POST["body"]
        print(request.FILES)
        if 'image' in request.FILES:
            image = request.FILES["image"]
            post.image = image

        post.title = title
        post.body = body

        post.save()
        return redirect('posts.index')

    return render(request, 'posts/edit.html', context={'post':post})

## delete
def delete(request, id):
    deleted = Post.delete_object(id)
    if deleted:
        return redirect('posts.index')
    return HttpResponse("object already deleted ")
