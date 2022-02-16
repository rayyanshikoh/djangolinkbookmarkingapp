from django.db import models

# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
