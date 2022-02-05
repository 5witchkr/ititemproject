from django.db import models

# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=25)
    image = models.TextField()
    content = models.TextField()
