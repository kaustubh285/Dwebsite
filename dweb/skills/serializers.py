from rest_framework import serializers
from .models import Programming_skill

class KaustubhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programming_skill
        fields = '__all__'