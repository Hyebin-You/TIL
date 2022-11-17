from .models import Profile_icon, Battlelog, Card, Rankcomment
from rest_framework import serializers

class BattlelogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Battlelog
        fields = '__all__'
        read_only_fields = ('user',)