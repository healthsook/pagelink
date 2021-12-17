from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from flask import Flask, request, render_template, flash, jsonify

def showlogin(request):
    return render(request, 'login.html')

def showhome(request):
    return render(request, 'home.html')

def signup_done(request):
    return render(request, 'signup_done.html')

def signup(request):
    if request.method == 'POST': 
        if request.POST['password1'] == request.POST['password2']: 
            user = User.objects.create_user( 
			        username=request.POST['username'], 
			        password=request.POST['password1'], 
			        email=request.POST['email'],
            )
            auth.login(request, user)
            #return redirect('/signup_done')
            return render(request, 'signup_done.html')
        return render(request, 'signup.html')
    else:
        form = UserCreationForm
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            flash("Done")
            return redirect('/')
        else:
            flash("아이디/비밀번호가 일치하지 않습니다.")
            return render(request, 'signup.html', {'error': 'username or password is incorrect.'})
    else:
        flash("login again")
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')