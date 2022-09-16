from rest_framework import serializers
from .models import Menstrual

class MenstrualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menstrual
        fields = ('id', 'bloody', 'date', 'flow', 'cramps', 'migraine', 'bloating', 'emo', 'anger', 'food', 'sex', 'nausea', 'sore', 'fatigue', 'aches', 'patriarchy')