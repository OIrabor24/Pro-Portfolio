from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/images')
    article = models.TextField() 
    link = models.URLField(max_length=100) 
    def __str__(self):
        return self.title
