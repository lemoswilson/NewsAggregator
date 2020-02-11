from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import FactMag_model
from .serializers import FactMagSerializer

class FactMag_news(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FactMag_model.objects.filter(category = "news").order_by("-date")
    serializer_class = FactMagSerializer
    filter_fields = ('is_highlight',)


class FactMag_tech(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FactMag_model.objects.filter(category = "tech").order_by("-date")
    serializer_class = FactMagSerializer
    filter_fields = ('is_highlight',)
# Create your views here.
