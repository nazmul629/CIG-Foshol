from django.shortcuts import render,redirect
from .models import *

def general_secretary(request):
    all_post = General_Secretary.objects.all()
    contex = {'details':all_post}
    return render(request,'home.html',contex)

