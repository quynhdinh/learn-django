from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120)
    intro = models.CharField(max_length=250)
    details = models.TextField()
    onGoing = models.BooleanField(default=False)


