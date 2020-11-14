from django.db import models
from django.utils import timezone

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255) #location name

    def __str__(self):
        return self.name

class Post(models.Model):
    subject = models.CharField(max_length=255) #title
    content = models.CharField(max_length=255) #content
    author = models.CharField(max_length=20) #author
    create_date = models.DateField(default=timezone.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject, self.content, self.author, self.create_date, self.location