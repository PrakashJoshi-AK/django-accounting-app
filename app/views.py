from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def home(request):
    return render(request, "app/home.html")
