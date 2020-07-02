from rest_framework import serializers
from .models import Program_skill, Project, Course, Certificate, Experience


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program_skill
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = "__all__"
