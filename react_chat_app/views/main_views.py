from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from react_chat_app.models import (
    Scream, Comment
)
from users.models import (
    User, Follow
)

@login_required
def blogView(request):
    users = User.objects.all()
    paginator = Paginator(
        users, per_page=2
    )
    page_no = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_no)
    
    context = {
        "paginator":paginator,
        "users" : page_obj.object_list,
    }
    return render(request, "react_chat_app/index.html", context)