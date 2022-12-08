# posts/models.py
from django.db import models

# Create your models here.
class Post(models.Model):  #new
    text = models.TextField()

    def __str__(self) -> str:  # new
        return self.text[:50]

    
