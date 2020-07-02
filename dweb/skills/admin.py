from django.contrib import admin

from .models import Program_skill, Project, Course, Certificate, Experience
# Register your models here.


admin.site.register(Program_skill)
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(Certificate)
admin.site.register(Experience)
