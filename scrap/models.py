from django.db import models

class Ranksite(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    selector = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name