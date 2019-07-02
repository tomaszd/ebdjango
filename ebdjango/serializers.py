from rest_framework import serializers
from .models import MatchResult
from .models import Player


class MatchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchResult
        fields = ('player1', 'player2', 'setWonPlayer1', 'setWonPlayer2', 'finished', 'tournament_name','pub_date','id')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name','id')
