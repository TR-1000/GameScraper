from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=60)
    image = models.URLField(max_length=2083)

    def __str__(self):
        return self.title
        return self.image
