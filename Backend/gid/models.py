from django.db import models

class Sight(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='sight_images')