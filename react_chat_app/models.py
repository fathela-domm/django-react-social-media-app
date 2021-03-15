from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from users.models import User
from django.shortcuts import reverse

# custom imports
import random
from string import (
    printable, whitespace
)

def unique_key():
    while True:
        code = "".join(
           random.choices(printable, k=50)
        ).strip(whitespace)
        if code != Scream.objects.filter(scream_code=code):
            break        
    return code

User = get_user_model()
class Scream(models.Model):
    scream_code = models.CharField(default=unique_key, max_length=50, null=True, blank=False)
    screams = models.TextField(null=True, blank=False, max_length=1000)
    date_created = models.DateTimeField(default=timezone.now, null=True, blank=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0, null=True, blank=False)
    dislikes = models.IntegerField(default=0, null=True, blank=False)

    @property
    def get_no_posts(self):
        return Post.objects.filter(id=self.id).count()

    def __str__(self):
        return "%s..." % (self.screams[:20])
    
    @property
    def no_of_comments(self):
        return Comment.objects.filter(scream_connected = self.id).count()

    @property
    def sender_image(self):
        return self.sender.image.url


class Post(models.Model):
    date_posted = models.DateTimeField(auto_now=True, auto_now_add=False)
    caption = models.CharField(max_length=100, null=True)
    post = models.FileField(upload_to="posts/%Y%M%D", max_length=100, blank=True)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name="posted_by", null=True)
    scream_connected = models.ForeignKey(Scream, on_delete=models.CASCADE, null=True)

    @property
    def get_comment(self):
        if Comment.post_connected:
            return Comment.objects.filter(id=self.id)
        else:
            return None

    @property
    def get_post(self):
        return f"{self.post.url}"

    class Meta:
        ordering = ["date_posted"]
        db_table = "posts"

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

""" In The Class Below All The Comments Are Defined """
class Comment(models.Model):
    comment = models.TextField(max_length=100, null=True, blank=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_posted  = models.DateTimeField(auto_now=True)
    scream_connected = models.ForeignKey(Scream, on_delete=models.CASCADE, null=True)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        ordering = ["date_posted"]
