
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class TechView(TemplateView):
    template_name = 'tech.html'

# Create your views here.
