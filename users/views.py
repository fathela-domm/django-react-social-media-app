from django.shortcuts import render, get_object_or_404, redirect
from . models import User
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings

class RegistrationForm(UserCreationForm):
    mobile_no = forms.CharField(label="Phone No", widget=forms.TextInput(
        attrs = {
            "class":"form-control form-group form ",
            "placeholder" : "Phone #..."
        }
    ))

    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs = {
            "class":"form-control form-group form ",
            "placeholder" : "Email..."
        }
    ))
   
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            "placeholder" : "Username...",
            "class" : "form-control form-group form",
        }
    ))

    handle = forms.CharField(label="Handle", widget=forms.TextInput(
        attrs={
            "placeholder" : "Handle...",
            "class" : "form-control form-group form",
        }
    ))
    class Meta:
        model = User
        fields = ["username", "mobile_no","email", "handle"]

class UserProfileUpdateForm(UserChangeForm):
    handle = forms.CharField( widget=forms.TextInput(
        attrs={
            "placeholder" : "Handle...",
            "class" : "form-control form-group form",
        }
    ))

    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            "placeholder" : "Username...",
            "class" : "form-control form-group form",
        }
    ))

    mobile_no = forms.CharField( widget=forms.TextInput(
        attrs={
            "placeholder" : "Phone #...",
            "class" : "form-control form-group form",
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder" : "Email...",
            "class" : "form-control form-group form",
        }
    ))

    class Meta:
        model = User
        fields = ["username","handle", "email", "mobile_no",  "image"]

def register(request):
    form = RegistrationForm
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(str(settings.LOGIN_REDIRECT_URL))
    id_ = ""
    for item in User.objects.all():
        if item.username == request.user.username:
            id_ = item.id

    return render(request, "user/register.html", {"form":form, "id":id_})

def update_user_profile(request, pk):
    queryset = get_object_or_404(User, id=pk)
    form = UserProfileUpdateForm(instance=queryset)
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, request.FILES,instance=queryset)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(str(settings.LOGIN_REDIRECT_URL))
    context = {
        "form" : form,
        "id": queryset.id,
    }
    return render(request, "user/register.html", context)
