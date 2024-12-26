from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic import CreateView, ListView, DetailView


# Create your views here.
class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'


class ProfileListView(ListView):
    template_name = 'profiles/user_profiles.html'
    model = UserProfile
    context_object_name = 'profiles'