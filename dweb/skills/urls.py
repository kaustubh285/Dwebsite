from rest_framework import routers
from .api import ProgrammingSkillViewSet

router = routers.DefaultRouter()

router.register('api/prgskills', ProgrammingSkillViewSet, 'ProgrammingSkills')

urlpatterns = router.urls