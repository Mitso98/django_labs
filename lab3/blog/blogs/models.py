from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_pub = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title + ' : ' + self.body
