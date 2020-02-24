from django.shortcuts import render
from .serializers import MixMagSerializer
from rest_framework import viewsets, mixins
from .models import MixMag_model

class MixMag_news(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MixMag_model.objects.filter(category="news").order_by("-date")
    serializer_class = MixMagSerializer

class MixMag_tech(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MixMag_model.objects.filter(category="tech").order_by("-date")
    serializer_class = MixMagSerializer