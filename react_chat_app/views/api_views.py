# django base imports
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.http import (
    HttpResponse, HttpResponseRedirect, JsonResponse
)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# Rest Framework imports
from rest_framework.parsers import JSONParser
from rest_framework import (
    permissions, viewsets
)
from rest_framework.decorators import (
    api_view, permission_classes, authentication_classes
)
from rest_framework.response import Response

# custom imports
from . serializers import (
    ScreamSerializer, ScreamSerializerGet, FollowSerializerGet,CommentSerializerGet, CommentSerializer, UserSerializer, GroupSerializer
)
from react_chat_app.models import (
    Comment, Scream, Post
)
from users.models import Follow
import requests, json

""" model class Comment api_views """
class CommentApiView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CreateComments(viewsets.generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# To view all posted comments

@permission_classes([permissions.IsAuthenticated])
@api_view(["GET", "POST"])
def getAllCommentApi(request):
    if request.user.is_authenticated:
        serializer = CommentSerializer
        if request.method == "GET":
            comment = Comment.objects.all()
            serializer = CommentSerializerGet(
                comment, many=True
            )
            return Response(
                serializer.data
            )
        elif request.method == "POST":
            serializer = CommentSerializer(
                data=request.data
            )    
            if serializer.is_valid():
                serializer.save()

            return Response(
                serializer.data
            )

    else:
        context = {
            "details": "AUTH details not provided",        
            "help text": "Please login as superuser to access the api.",
        }
        return Response(
            context

)
@permission_classes([permissions.IsAuthenticated])
@api_view(["GET"])
def getCommentDetail(request, pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializerGet(
            comment, many=False
        )
        return Response(
            serializer.data
        )

    else:
        context = {
            "details": "AUTH details not provided",        
            "help text": "Please login as superuser to access the api.",
        }
        return Response(
            context

)
@api_view(["PUT", "GET"])
@permission_classes([permissions.IsAuthenticated])
def updateAComment(request, pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer
        if request.method == "PUT":
            serializer = CommentSerializer(
                    instance=comment, data=request.data
            )    
            if serializer.is_valid():
                serializer.save()
           
        elif request.method == "GET":
            serializer = CommentSerializerGet(
                    comment, many=False
            )  
        return Response(
            serializer.data
        )


    else:
        context = {
            "details": "AUTH details not provided",        
            "help text": "Please login as superuser to access the api.",
        }
        return Response(
            context

)
@api_view(["GET", "DELETE"])
@permission_classes([permissions.IsAuthenticated])
def deleteAComment(request, pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=pk)
        if request.method == "DELETE":
            comment.delete()
            return Response(
               str(comment.comment[:20]) + " successfully deleted"
            )

        elif request.method == "GET":
            serializer = CommentSerializerGet(
                    comment, many=False
                )
            return Response(
                serializer.data
            )

    else:
        context = {
            "details": "AUTH details not provided",        
            "help text": "Please login as superuser to access the api.",
        }
        return Response(
            context
            )

""" model class User api views """
User = get_user_model()
class CreateUser(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by("date_joined")
    serializer_class = UserSerializer

""" model class Group api view """
class CreateGroup(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
""" Scream api view """
class CreateScream(viewsets.generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Scream.objects.all()
    serializer_class = ScreamSerializer

@permission_classes([permissions.IsAuthenticated])
@api_view(["GET"])
def getAllScreamApi(request):
    if request.user.is_authenticated:
        scream =Scream.objects.all()
        serializer =ScreamSerializerGet(
        scream, many=True
        )
        return Response(
            serializer.data
        )
    
    else:
        context = {
            "details": "AUTH details not provided.",            
            "help text": "Please login as superuser to access the api.",
        }
        return Response(
            context
        )

@permission_classes([permissions.IsAuthenticated])
@api_view(["GET"])
def getScreamDetail(request, pk):
    if request.user.is_authenticated:
        scream = get_object_or_404(Scream, id=pk)
        serializer =ScreamSerializerGet(
        scream, many=False
        )
        return Response(
            serializer.data
        )

    else:
        context = {
            "details": "AUTH details not provided",        
            "help text": "Please login as superuser to access the api.",
        }
        return Response(
            context
        )

@api_view(["PATCH", "GET", "POST"])
@permission_classes([permissions.IsAuthenticated])
def updateAScream(request, pk):
    if request.user.is_authenticated:
        scream = get_object_or_404(Scream, id=pk)
        serializer =ScreamSerializer
        if request.method == "PATCH" or request.method == "POST":
            serializer =ScreamSerializer(
                    instance=scream, data=request.data
            )    
            if serializer.is_valid():
                serializer.save()

            else:
                print("Error")

        elif request.method == "GET":
            serializer =ScreamSerializerGet(
                scream, many=False
            )  
    
        return Response(
            serializer.data
        )
    
    else:
        context = {
            "details": "AUTH details not provided.",            
            "help text": "Please login as superuser to access the api.",
        }
        return Response(
            context
        )

@api_view(["GET", "DELETE"])
@permission_classes([permissions.IsAuthenticated])
def deleteAScream(request, pk):
    if request.user.is_authenticated:
        scream = Scream.objects.get(id=pk)
        if request.method == "DELETE":
            scream.delete()

        serializer =ScreamSerializerGet(
                scream, many=False
                )
        if serializer.data:
            return Response(
               serializer.data
            )
        else:
            return Response(
                "successfully deleted"
                )
    
    else:
        context = {
            "details": "AUTH details not provided.",            
            "help text": "Please login as superuser to access the api.",
        }
        return Response(
            context
        )

from .serializers import PostSerializer, PostSerializerGet
""" All models api """
@authentication_classes(permissions.IsAuthenticated)
@api_view(["GET"])
def chatApi(request):
    if request.user.is_authenticated:
        comment = Comment.objects.all().order_by("-date_posted")
        comment_serializer = CommentSerializerGet(
            comment, many=True
        )

        follow = Follow.objects.all()
        follow_serializer = FollowSerializerGet(
            follow, many=True
        )

        scream = Scream.objects.all().order_by("-date_created")
        scream_serializer = ScreamSerializerGet(
            scream, many=True
        )
        post = Post.objects.all().order_by("-date_posted")
        post_serializer = PostSerializerGet(
            post, many=True
        )
        context = {
            "comments" : comment_serializer.data,
            "screams" : scream_serializer.data,
            "followers": follow_serializer.data,
            "post": post_serializer.data,
        }
        return Response(
            context
        )
    else:
        context = {
            "details" : "Authentication credentials were not provided.",
            "help text": "Please login to access The APi",
        }

        return Response(
            context
        )

class ViewPosts(viewsets.generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializerGet

class CreatePosts(viewsets.generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


from .serializers import FollowSerializer
class FollowApiView(viewsets.generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer