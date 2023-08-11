from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView
# from django.contrib.auth.decorators
# Create your views here.
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ModefiedUserForm

class AccountProfile(View):
    def get(self, request):
        return HttpResponse("<h1> welcome to your profile</h1>")


class RegisterAccount(CreateView):
    model =  User
    template_name = 'accounts/register.html'
    success_url = '/students'
    form_class = ModefiedUserForm

