from rest_framework import serializers
from .models import Program_skill

class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Program_skill
        fields = "__all__"