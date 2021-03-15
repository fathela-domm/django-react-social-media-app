from django.urls import path
from react_chat_app.views.main_views import *

urlpatterns = [
    path("", blogView, name="blog")
]