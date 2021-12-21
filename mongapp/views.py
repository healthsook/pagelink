from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'home.html', context)
    
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

def test2(request):
    return render(request, 'test2.html')

def test3(request):
    return render(request, 'test3.html')

def result(request):
    return render(request, 'result.html')

def myinfo(request):
    return render(request, 'myinfo.html')

def chid(request):
    return render(request, 'chid.html')

def chpw(request):
    return render(request, 'chpw.html')