from django.db import models
from django.utils import timezone
import json


# Create your models here.
class FactMag_model(models.Model):
    link = models.CharField(max_length=300, default=None)
    headline = models.CharField(max_length=300, unique=True, default=None)
    description = models.CharField(max_length=300, default=None)
    date = models.DateTimeField(default=timezone.now()) # date format = dd.mm.yy / "%d.%m.%y"
    is_highlight = models.CharField(max_length=1, default=None)
    tags = models.CharField(max_length=200, default=None) 
    def set_tags(self, x):
        self.tags = json.dumps(x)

    def get_tags(self):
        return json.loads(self.tags)
    
    category = models.CharField(max_length=10, default=None)


    
