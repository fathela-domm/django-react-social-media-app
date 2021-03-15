from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class User(AbstractUser):
    image = models.ImageField(upload_to = "user_profile_pics", default="default.png", null=True, blank=True, help_text="User Image")
    mobile_no = models.CharField(null=True, blank=False, max_length=50)
    handle = models.CharField(null=True, blank=False, max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    date_last_modified = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        
        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            image.thumbnail((300,300))
            image.save(self.image.path)

    def __str__(self):
        return self.username

    @property
    def following(self):
        return Follow.objects.filter(follower=self.id).count()

    @property
    def followers(self):
        return Follow.objects.filter(following=self.id).count()

    class Meta:
        ordering = ["date_joined"]
        db_table = "user"

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "follow_idol", null=True)
    date_you_followed = models.DateField(auto_now_add=True)