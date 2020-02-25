from django.shortcuts import render
from .serializers import ResidentAdvisorSerializer
from rest_framework import viewsets, mixins
from .models import ResidentAdvisor_model

class ResidentAdvisor_news(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ResidentAdvisor_model.objects.all().order_by("-date")[:15]
    serializer_class = ResidentAdvisorSerializer
    filter_fields = ("featured",)
# Create your views here.
