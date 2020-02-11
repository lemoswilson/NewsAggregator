from rest_framework import serializers
from .models import MixMag_model

class MixMagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MixMag_model
        fields = ("link", "headline", "description", "date", "tags", "category")