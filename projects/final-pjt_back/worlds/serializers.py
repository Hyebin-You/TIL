from .models import Profile_icon, Battlelog, Card, Rankcomment
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Usercard, Attacklist, Defenselist


User = get_user_model()


class BattlelogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Battlelog
        fields = '__all__'
        read_only_fields = ('user', 'enermy_nickname')


class UsercardSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usercard
        fields = ('isnormal', 'img_url', 'ability_grade')


class AttacklistSimpleSerializer(serializers.ModelSerializer):
    card1 = UsercardSimpleSerializer(read_only=True)
    card2 = UsercardSimpleSerializer(read_only=True)
    card3 = UsercardSimpleSerializer(read_only=True)

    class Meta:
        model = Attacklist
        fields = '__all__'
        read_only_fields = ('user',)


class DefenselistSimpleSerializer(serializers.ModelSerializer):
    card1 = UsercardSimpleSerializer(read_only=True)
    card2 = UsercardSimpleSerializer(read_only=True)
    card3 = UsercardSimpleSerializer(read_only=True)

    class Meta:
        model = Defenselist
        fields = '__all__'
        read_only_fields = ('user',)


class RankSerializer(serializers.ModelSerializer):
    attacklist_set = AttacklistSimpleSerializer(many=True, read_only=True)
    defenselist_set = DefenselistSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'tier', 'win_point', 'attacklist_set', 'defenselist_set', 'user_icon')
        read_only_fields = ('username', 'nickname', 'tier', 'win_point',)


class RankcommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rankcomment
        fields = '__all__'


class ProfiliconSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile_icon
        fields = '__all__'