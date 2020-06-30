from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SkillSerializer, ProjectSerializer
from .models import Program_skill, Project

class Prg_skills(APIView):
    
    def get(self, request):
        my_skills = Program_skill.objects.all()
        serializer = SkillSerializer(my_skills, many = True)
        return Response(serializer.data)
    
    def post(self):
        pass

class MyProjects(APIView):
    
    def get(self, request):
        my_projects = Project.objects.all()
        serializer = ProjectSerializer(my_projects, many = True)
        return Response(serializer.data)
    
    def post(self):
        pass