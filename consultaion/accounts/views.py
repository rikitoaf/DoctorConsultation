from math import ceil

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect


def home (request):
    return render(request,'accounts/index.html')