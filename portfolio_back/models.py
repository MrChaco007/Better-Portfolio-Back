from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    img_url = models.URLField(max_length=600)
    github = models.URLField(max_length=600)
    live = models.URLField(max_length=600)
    ruby = models.BooleanField()
    python = models.BooleanField()
    javascript = models.BooleanField()
    react = models.BooleanField()
    jquery = models.BooleanField()
    express = models.BooleanField()
    rails = models.BooleanField()
    django = models.BooleanField()

    class Meta:
        verbose_name_plural = 'projects'