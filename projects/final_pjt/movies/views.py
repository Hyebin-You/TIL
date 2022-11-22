import random
from .models import Movie, Genre, Playlist, Review
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer, MovieListSerializer, MovieSerializer
from .serializers import ReviewSimpleSerializer, PlaylistSerializer, PlaylistCreateSerializer

# Create your views here.
@api_view(['GET'])      # 영화들 검색
def movie_list(request, search_type):
    if search_type == 'latest':
        # 11/20 최신 영화 중 예고편 키가 있는 것만 정렬해서 보내게 수정
        movies = Movie.objects.exclude(video_key='').order_by('-release_date')
        movies = movies.exclude(overview='')
        movies = movies.exclude(title='')
        movies = list(movies)[:20]
        serializer = MovieListSerializer(movies, many=True)
        
    elif search_type == 'genre':
        genre_name = request.GET.get('genre')
        genre = Genre.objects.get(name=genre_name)
        movies = genre.movies.all()
        movies = movies.exclude(overview='')
        movies = movies.exclude(title='')
        movies = movies.exclude(video_key='')
        serializer = MovieListSerializer(movies, many=True)
                  
    elif search_type == 'random':
        movies = Movie.objects.all()
        movies = movies.exclude(overview='')
        movies = movies.exclude(title='')
        movies = movies.exclude(video_key='')
        movies = random.sample(list(movies), 20)
        serializer = MovieListSerializer(movies, many=True)
    else:
        query = request.GET.get('query')
        movies = Movie.objects.all()
        movies = movies.exclude(overview='')
        movies = movies.exclude(title='')
        movies = movies.exclude(video_key='')
        movies = movies.filter(title__contains=query)
        serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])      # 영화 상세
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])     # 영화 좋아요
def likes(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        movie.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)


@api_view(['POST'])     # 리뷰 생성
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        r_serializer = ReviewSimpleSerializer(movie.review_set.all(), many=True)
        return Response(r_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])     # 리뷰 상세 조회, 수정, 삭제
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'GET':
        serializer = ReviewSimpleSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_playlist(request):       # 보관함 생성
    serializer = PlaylistCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)
        

@api_view(['DELETE'])
def delete_playlist(request, playlist_id):      # 보관함 삭제
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    playlist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def playlist_movie(request, playlist_id, movie_id):         # 보관함에 영화 담기, 빼기
    movie = get_object_or_404(Movie, pk=movie_id)
    playlist = get_object_or_404(Playlist, pk=playlist_id)

    if movie.playlists.filter(pk=playlist.pk).exists():
        movie.playlists.remove(playlist)
        in_playlist = False
    else:
        movie.playlists.add(playlist)
        in_playlist = True
    context = {
        'in_playlist': in_playlist,
    }
    return JsonResponse(context)


@api_view(['GET'])
def all_playlists(request):         # 존재하는 모든 플레이리스트 정보 반환
    playlists = Playlist.objects.filter(isopened=True)
    serializer = PlaylistSerializer(playlists, many=True)
    return Response(serializer.data)


@api_view(['GET'])      # 해당 유저가 가진 플레이리스트들 반환
def user_playlists(request):
    user = request.user
    playlists = user.playlist_set.all()
    serializer = PlaylistSerializer(playlists, many=True)
    return Response(serializer.data)


@api_view(['GET'])      # 특정 플레이리스트 detail (리스트 안의 영화들과 공개정보)
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    serializer = PlaylistSerializer(playlist)
    return Response(serializer.data)