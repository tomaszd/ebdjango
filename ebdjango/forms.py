from django import forms

from .models import MatchResult


class MatchResultForm(forms.ModelForm):
    class Meta:
        model = MatchResult
        fields = ('player1', 'player2', 'setWonPlayer1', 'setWonPlayer2', 'finished', 'tournament_name')
        labels = {
            'player1': "Player 1",
            'player2': "Player 2",
            "setWonPlayer1": "sets won by Player 1",
            "setWonPlayer2": "sets won by Player 2"
        }
