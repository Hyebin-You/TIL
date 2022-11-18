from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('user_detail/', views.user_detail, name='user_detail'),
    path('make_usercards/', views.make_usercards, name='make_usercards'),
    path('make_attacklist/', views.make_attacklist, name='make_attacklist'),
    path('make_defenselist/', views.make_defenselist, name='make_defenselist'),
    path('set_nickname/', views.set_nickname, name='set_nickname'),
]
