from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

# Create your models here.

class Programming_skill(models.Model):
    title = models.CharField(max_length=150)
    level = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1),MaxValueValidator(10)]
    )

