from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    member = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=250, blank=False)
    created_on = models.DateTimeField(default=timezone.now)
