from django.contrib import admin
from . models import User, Follow

class AdminForm(admin.ModelAdmin):
    list_display = ["username","handle", "following", "followers","date_joined", "mobile_no","is_staff", "is_authenticated"]
    filter = ["username"]
    search_fields = ["username"]

class FollowAdminForm(admin.ModelAdmin):
    list_display = ["follower", "following", "date_you_followed"]
    filter = ["follower"]
    search_fields = ["follower"]

admin.site.register(User, AdminForm)
admin.site.register(Follow, FollowAdminForm)