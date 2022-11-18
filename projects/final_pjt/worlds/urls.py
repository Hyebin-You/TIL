from django.urls import path
from . import views

app_name = 'worlds'

urlpatterns = [
    path('ranklist/', views.ranklist, name='ranklist'),
    path('make_battlelog/', views.make_battlelog, name='make_battlelog'),
    path('rankcomment_list/', views.rankcomment_list, name='rankcomment_list'),
    path('create_rankcomment/', views.create_rankcomment, name='create_rankcomment'),
    path('buy_cube/', views.buy_cube, name='buy_cube'),
    path('change_tier/', views.change_tier, name='change_tier'),
]
