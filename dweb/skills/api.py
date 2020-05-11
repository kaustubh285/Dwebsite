from .models import Programming_skill
from rest_framework import viewsets, permissions
from .serializers import KaustubhSerializer

class ProgrammingSkillViewSet(viewsets.ModelViewSet):
    queryset = Programming_skill.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = KaustubhSerializer