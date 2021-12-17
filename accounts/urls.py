from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('showogin/', views.showlogin, name='showlogin'),
    path('showhome/', views.showhome, name='showhome'),
    path('singup_done', views.signup_done, name="signup_done")
]