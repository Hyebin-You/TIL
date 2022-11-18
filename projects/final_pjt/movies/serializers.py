from rest_framework import serializers
from .models import Movie, Genre, Playlist, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'score')
        read_only_fields = ('movie', 'user')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)

    
class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'vote_average', 'genres')


class ReviewSimpleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = ('title', 'content', 'score')


class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSimpleSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        exclude = ('id', 'playlists')


class PlaylistCreateSerializer(serializers.ModelSerializer):
    in_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ('isopened', 'in_movies')
        read_only_fields = ('user',)


class PlaylistSerializer(serializers.ModelSerializer):
    in_movies = MovieListSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ('id', 'isopened', 'in_movies')
        read_only_fields = ('user',)