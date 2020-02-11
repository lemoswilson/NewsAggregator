from rest_framework import serializers
from .models import FactMag_model

class FactMagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactMag_model
        fields = ("link", "headline", "description", "date", "is_highlight", "tags", "category")