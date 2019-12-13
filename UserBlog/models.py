from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    Slug = models.SlugField(default=True)
    date_published = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='picture/%Y/%m/', blank=True, null=True)
    file = models.FileField(upload_to='files/%Y/%m/',blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def approve(self):
        self.active = True
        self.save()

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
