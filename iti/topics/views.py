from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from topics.models import Topic


## import newly created form ?
from topics.forms import TopicForm, TopicModelForm

def create(request):
    myform = TopicForm()
    if request.method =='POST':
        print(request.POST)
        name = request.POST['name']
        logo= None
        if request.FILES:
            logo = request.FILES['logo']
        topic = Topic.objects.create(name=name, logo=logo)
        return HttpResponse("data received")

    return render(request, 'topics/create.html', context={"form":myform})




def create_via_model(request):
    form  = TopicModelForm()
    if request.method=='POST':
        form = TopicModelForm(request.POST, request.FILES)
        if form.is_valid():
            topic=form.save()
            # return HttpResponse(topic.name)
            return redirect('topics.index')
        # return HttpResponse("not valid")
    return render(request, 'topics/create.html',context={"form":form})


def index(request):
    topics = Topic.get_all_objects()
    return render(request, 'topics/index.html',context={'topics':topics})



def edit(request, id):
    topic = Topic.get_specific_object(id)
    form = TopicModelForm(instance=topic)
    if request.POST:
        form = TopicModelForm(request.POST, request.FILES, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topics.index')


    return render(request, 'topics/edit.html', context={'form': form})

