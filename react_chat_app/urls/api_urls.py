# This module handles the creation of api endpoint urls which are def in views.api_views.py module

from django.urls import path, include
from react_chat_app.views.api_views import (
    CommentApiView, getAllCommentApi, getCommentDetail, CreateComments, updateAComment, deleteAComment,
    getAllScreamApi, getScreamDetail, CreateScream, updateAScream, deleteAScream,
    chatApi,CreateUser,CreateGroup,FollowApiView, ViewPosts, CreatePosts
)
from rest_framework import routers

# Routing in the django rest framework
router = routers.DefaultRouter()
router.register(r"user", CreateUser)
router.register(r"group", CreateGroup)

urlpatterns = [
    path("create_comments/", CreateComments.as_view(), name="create_comments"),
    path("comment_detail/<str:pk>/", getCommentDetail, name="get-comment-detail"),
    path("update_a_comment/<str:pk>/", updateAComment, name="update_a_comment"),
    path("delete_a_comment/<str:pk>/", deleteAComment, name="delete_a_comment"),

    path("groups_or_users/", include(router.urls)),
  
    path("create_screams/", CreateScream.as_view(), name="create_Scream"),
    path("scream_detail/<str:pk>/", getScreamDetail, name="get-Scream-detail"),
    path("update_a_scream/<str:pk>/", updateAScream, name="update_a_Scream"),
    path("delete_a_scream/<str:pk>/", deleteAScream, name="delete_a_Scream"),

    path("create_posts/", CreatePosts.as_view(), name="create_posts"),

    path("", chatApi, name="chat-api"),
    path("follow/", FollowApiView.as_view(), name="follow"),
    path("api_auth/", include("rest_framework.urls", namespace="rest_framework"))
]