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