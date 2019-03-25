from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=80, blank=True, default="", primary_key=True)
    image = models.TextField()
