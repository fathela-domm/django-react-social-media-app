from react_chat_app.models import (
    Scream, Comment, Post
)
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from users.models import (
    User, Follow
)

class ScreamSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    scream_code = serializers.CharField(read_only=True)
    class Meta:
        model = Scream
        fields = "__all__"


class ScreamSerializerGet(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    scream_code = serializers.CharField(read_only=True)
    no_of_comments = serializers.IntegerField(read_only=True)
    sender = serializers.CharField(read_only=True)
    sender_image = serializers.CharField(read_only=True)
   
    class Meta:
        model = Scream
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializerGet(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)
    sender = serializers.CharField(read_only=True)
    scream_connected = serializers.CharField(read_only=True)
    post_connected = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

class FollowSerializerGet(serializers.ModelSerializer):
    following = serializers.CharField(read_only=True)
    follower = serializers.CharField(read_only=True)
    class Meta:
        model = Follow
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    date_last_modified = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = [
            "id", "username", "email", "handle", "mobile_no","date_joined","image","url", "groups", "date_last_modified","following", "followers",
        ]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            "id", "name","url"
        ]


class PostSerializerGet(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    posted_by = serializers.CharField(read_only=True)
    scream_connected = serializers.CharField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields ="__all__"


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields ="__all__"