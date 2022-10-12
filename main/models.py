from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150, unique=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    slug=models.SlugField(max_length=255)
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])


class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2083, default="", unique=True)
    published = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-published']

    def __str__(self):
        return self.title