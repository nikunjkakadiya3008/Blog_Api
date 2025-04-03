from django.db import models
from django.conf import settings

class Post(models.Model):
    status_choices = {
        'draft':'draft',
        'published':'published'
    }
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(blank = True , null=True)
    updated_at = models.DateTimeField(blank=True , null= True)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=25 , choices=status_choices)
    Category = models.ManyToManyField('Category')
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
