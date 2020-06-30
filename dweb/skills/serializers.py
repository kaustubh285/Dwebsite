from rest_framework import serializers
from .models import Program_skill, Project

class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Program_skill
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = "__all__"