from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import SearchForm
from .forms import RecordForm
from .models import Record, Mongs
from django.urls import reverse
from datetime import datetime
from accounts.models import Users
# Create your views here.

def home(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'home.html', context)
    
def information(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'infor.html', context)

def myshop(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'myshop.html', context)

def mongs(request):
    login_session = request.session.get('login_session', '')
    q = Mongs.objects.order_by('-id')
    context = { 'login_session' : login_session }
    return render(request, 'mongs.html', {'quiz':q, 'login_session':login_session})

def record(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'record.html', context)

def test(request):
    login_session = request.session.get('login_session', '')
    form = SearchForm(request.POST or None)
    if request.method =="POST":
        if form.is_valid():
            배 = request.POST.get("배", None)
    return render(request, 'test.html', {"form":form, 'login_session':login_session})

def test2(request):
    login_session = request.session.get('login_session', '')
    form = SearchForm(request.POST or None)
    if request.method =="POST":
        if form.is_valid():
            배 = request.POST.get("배", None)
    return render(request, 'test2.html', {"form":form, 'login_session':login_session})

def test3(request):
    login_session = request.session.get('login_session', '')
    form = SearchForm(request.POST or None)
    if request.method =="POST":
        if form.is_valid():
            배 = request.POST.get("배", None)
    return render(request, 'test3.html', {"form":form, 'login_session':login_session})

def result(request):
    login_session = request.session.get('login_session', '')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        body = request.POST.getlist('체형[]')
        talent = request.POST.getlist('소질[]')
        character = request.POST.getlist('성격[]')
        total = [body, talent, character]
        maxlen = []
        whole = []
        taey = []
        taeum = []
        soy = []
        soum = []


        if form.is_valid():
            i=0
            while i<len(total):
                j=0
                while j<len(total[i]):
                    if total[i][j] == '태양인':
                        taey.append(total[i][j])
                    elif total[i][j] == '태음인':
                        taeum.append(total[i][j])
                    elif total[i][j] == '소양인':
                        soy.append(total[i][j])
                    elif total[i][j] == '소음인':
                        soum.append(total[i][j])
                    j += 1
                i += 1
            maxlen.append(len(taey))
            maxlen.append(len(taeum))
            maxlen.append(len(soy))
            maxlen.append(len(soum))
            if max(maxlen) == len(taey):
                whole.append('태양인')
            elif max(maxlen) == len(taeum):
                whole.append('태음인')
            elif max(maxlen) == len(soy):
                whole.append('소양인')
            elif max(maxlen) == len(soum):
                whole.append('소음인')
            return render(request, 'birth_load.html', {'whole': whole}) #피그마 '체질몽 탄생' 만든거 파일명 birth_load입니당
    else:
        form = SearchForm()
        return render(request, 'test.html', {'login_session':login_session})

def mymong(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    cons = Users.objects
    monguser = Users.objects.get(user_id=login_session)
    return render(request, 'mymong.html', {'login_session' : login_session, 'cons' : cons})

def chid(request):
    return render(request, 'chid.html')

def chpw(request):
    return render(request, 'chpw.html')

def result_ty(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'result_ty.html', context)

def result_te(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'result_te.html', context)

def result_sy(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'result_sy.html', context)

def result_se(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'result_se.html', context)

def birth_load(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'birth_load.html', context)

def birth_ty(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'birth_ty.html', context)

def birth_te(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'birth_te.html', context)

def birth_sy(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'birth_sy.html', context)

def birth_se(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'birth_se.html', context)

def info_ty(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'info_ty.html', context)

def info_te(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'info_te.html', context)

def info_sy(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'info_sy.html', context)

def info_se(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'info_se.html', context)

def index(request):
    login_session = request.session.get('login_session', '')
    post_list = Record.objects.all()
    return render(request, 'index.html', { 'login_session' : login_session, 'post_list': post_list })

def create(request):
    login_session = request.session.get('login_session', '')
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecordForm()
    return render(request, 'create.html', {'form': form, 'login_session' : login_session})

def detail(request, post_id):
    login_session = request.session.get('login_session', '')
    record = get_object_or_404(Record, pk=post_id)
    return render(request, 'detail.html', {'post': record, 'login_session' : login_session})

def update(request, post_id):
    login_session = request.session.get('login_session', '')
    record = get_object_or_404(Record, pk=post_id)

    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = RecordForm(instance=record)
    return render(request, 'update.html', {'form': form, 'login_session' : login_session})

def delete(request, post_id):
    login_session = request.session.get('login_session', '')
    record = Record.objects.get(pk=post_id)
    record.delete()
    return redirect('index')

def mymong_ty(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'mymong_ty.html', context)
    
def mymong_te(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'mymong_te.html', context)

def mymong_sy(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'mymong_sy.html', context)

def mymong_se(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    return render(request, 'mymong_se.html', context)