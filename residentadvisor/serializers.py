from rest_framework import serializers
from .models import ResidentAdvisor_model

class ResidentAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentAdvisor_model
        fields = ("link", "headline", "description", "date", "tags", "featured",)

