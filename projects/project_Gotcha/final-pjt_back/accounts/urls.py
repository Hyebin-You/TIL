from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('user_detail/', views.user_detail, name='user_detail'),
    path('make_usercards/', views.make_usercards, name='make_usercards'),
    path('make_attacklist/', views.make_attacklist, name='make_attacklist'),
    path('make_defenselist/', views.make_defenselist, name='make_defenselist'),
    path('set_nickname/', views.set_nickname, name='set_nickname'),
    path('set_like_genres/<str:genre_name>/', views.set_like_genres, name='set_like_genres'),
    path('modify_card/', views.modify_card, name='modify_card'),
    path('use_cube/', views.use_cube, name='use_cube'),
    path('buy_icon/', views.buy_icon, name='buy_icon'),
    path('change_usericon/', views.change_usericon, name='change_usericon'),
    path('change_point/', views.change_point, name='change_point'),
]
