
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

def home(request):
    return render(request, "news/home.html")


# Create your views here.
