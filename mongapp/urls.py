from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('infor/', information, name="information"),
    path('mypage/', mypage, name="mypage"),
    path('mongs/', mongs, name="mongs"),
    path('record/', record, name="record"),
    path('test/', test, name="test"),
    path('test2/', test2, name="test2"),
    path('test3/', test3, name="test3"),
    path('result/', result, name="result"),
    path('myinfo/', myinfo, name="myinfo"),
    path('chid/', chid, name="chid"),
    path('chpw/', chpw, name="chpw"),
]