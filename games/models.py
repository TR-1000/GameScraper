from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=60)
    image = models.URLField(max_length=2083)
    name = models.CharField(max_length=60, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title
        return self.image
        return self.name
        return self.comment
