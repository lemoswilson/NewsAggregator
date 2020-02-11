from django.db import models
from django.utils import timezone

class ResidentAdvisor_model(models.Model):
    link = models.CharField(max_length = 300, default = None)
    headline = models.CharField(max_length = 300, unique = True, default = None)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now())
    tags = models.CharField(max_length = 100)
    is_featured = models.BooleanField()

    