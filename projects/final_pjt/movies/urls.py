from django.urls import path
from . import views
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name='movies'
urlpatterns = [
    path('search/<str:search_type>/', views.movie_list, name='movie_list'),
    path('movie_detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('likes/<int:movie_id>/', views.likes, name='likes'),
    path('create_review/<int:movie_id>/', views.create_review, name='create_review'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('delete_playlist/<int:playlist_id>/', views.delete_playlist, name='delete_playlist'),
    path('playlist_movie/<int:playlist_id>/<int:movie_id>/', views.playlist_movie, name='playlist_movie'),
    path('getallplaylists/', views.all_playlists, name='all_playlists'),
    path('user_playlists/', views.user_playlists, name='user_playlists'),
    path('playlist_detail/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]