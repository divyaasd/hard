from django.db import models
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Assuming you have a URL pattern named 'post_detail' that takes the post's primary key (pk) as an argument
        return reverse('blogpost_detail', kwargs={'pk': self.pk})
class Empty(models.Model):
    name=models.CharField(max_length=100)