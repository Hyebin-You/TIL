from .models import Usercard, Attacklist, Defenselist
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import PlaylistSerializer
from worlds.serializers import BattlelogSerializer

User = get_user_model()


class UsercardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usercard
        fields = '__all__'


class AttacklistSerializer(serializers.ModelSerializer):
    card1 = UsercardSerializer(read_only=True)
    card2 = UsercardSerializer(read_only=True)
    card3 = UsercardSerializer(read_only=True)

    class Meta:
        model = Attacklist
        fields = '__all__'
        read_only_fields = ('user',)


class DefenselistSerializer(serializers.ModelSerializer):
    card1 = UsercardSerializer(read_only=True)
    card2 = UsercardSerializer(read_only=True)
    card3 = UsercardSerializer(read_only=True)

    class Meta:
        model = Defenselist
        fields = '__all__'
        read_only_fields = ('user',)


class CustomUserdetailSerializer(serializers.ModelSerializer):
    playlist_set = PlaylistSerializer(many=True)
    attacklist_set = AttacklistSerializer(read_only=True)
    defenselist_set = DefenselistSerializer(read_only=True)
    battlelog_set = BattlelogSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'point', 'tier', 'win_point', 'blackcude', 'redcude', 'playlist_set', 'attacklist_set', 'defenselist_set', 'battlelog_set')