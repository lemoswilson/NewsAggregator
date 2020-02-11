from rest_framework import serializers
from .models import Pitchfork_model

class PitchforkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitchfork_model
        fields = ("link", "headline", "description", "date", "tags")