from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Pitchfork_model
from .serializers import PitchforkSerializer

class Pitchfork_news(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Pitchfork_model.objects.all().order_by("-date")
    serializer_class = PitchforkSerializer

# Create your views here.
