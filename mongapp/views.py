from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'home.html')

def information(request):
    return render(request, 'infor.html')

def mypage(request):
    return render(request, 'mypage.html')

def mongs(request):
    return render(request, 'mongs.html')

def record(request):
    return render(request, 'record.html')

def test(request):
    return render(request, 'test.html')

def result(request):
    return render(request, 'result.html')

def myinfo(request):
    return render(request, 'myinfo.html')

def chid(request):
    return render(request, 'chid.html')

def chpw(request):
    return render(request, 'chpw.html')