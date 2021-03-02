from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    img_url = models.URLField(max_length=600)

    class Meta:
        verbose_name_plural = 'projects'