from django.shortcuts import render
from django.views.generic import View
from .models import User

# Create your views here.

class UserViews(View):
    """
    views for user
    """
    def get():
        return User.objects.all()