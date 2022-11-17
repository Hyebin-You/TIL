from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('user_detail/', views.user_detail, name='user_detail'),
    path('make_attacklist/', views.make_attacklist, name='make_attacklist'),
]
