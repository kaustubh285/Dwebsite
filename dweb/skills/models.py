from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Program_skill(models.Model):
    title = models.CharField(max_length = 150, verbose_name='Title')
    level = models.IntegerField(
        default = 1,
        validators = [
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return 'Skill: '+str(self.title)+', Level : '+str(self.level)

class Project(models.Model):
    title = models.CharField(max_length = 150, verbose_name='Title')
    description = models.TextField(verbose_name="Description")
    git_url = models.CharField(max_length = 250, verbose_name='Git Url')
    hosted_url = models.CharField(max_length = 250, verbose_name='Hosted Url') 
    date = models.DateField(auto_now=False, auto_now_add=False) 

    def __str__(self):
        return 'Project: '+str(self.title)