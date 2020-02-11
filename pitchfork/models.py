from django.db import models
from django.utils import timezone
import json

class Pitchfork_model(models.Model):
    link = models.CharField(max_length = 300, default = None)
    headline = models.CharField(max_length = 300, default = None)
    description = models.CharField(max_length = 300, default = None)
    date = models.DateTimeField(default = timezone.now())

    tags = models.CharField(max_length = 1000, default = None)
    def set_tags(self, x):
        self.tags = json.dumps(x)

    def get_tags(self):
        return json.loads(self.tags)

