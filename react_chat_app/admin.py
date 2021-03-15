from django.contrib import admin
from . models import Scream, Comment, Post

class ScreamAdminForm(admin.ModelAdmin):
    search_fields = ["sender"]
    filter = ["date_created"]
    list_display =[Scream.__str__, "id", "no_of_comments","sender", "dislikes", "likes", "get_no_posts","date_created"]

class CommentAdminForm(admin.ModelAdmin):
    list_display = ["id", "comment", "sender","date_posted","scream_connected"]
    filter = ["date_posted"]
    search_fields = ["comment", "sender"]

class PostAdminForm(admin.ModelAdmin):
    list_display = ["caption", "date_posted", "posted_by", "get_post", "scream_connected"]
    filter = ["date_posted"]
    search_fields = ["caption"]

admin.site.register(Scream, ScreamAdminForm)
admin.site.register(Comment, CommentAdminForm)
admin.site.register(Post, PostAdminForm)
