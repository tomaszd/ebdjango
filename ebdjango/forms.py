from django import forms

from .models import MatchResult


class MatchResultForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatchResultForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MatchResult
        fields = ('player1', 'player2', 'setWonPlayer1', 'setWonPlayer2', 'finished', 'tournament_name', 'game_type')
        labels = {
            'player1': "Player 1",
            'player2': "Player 2",
            "setWonPlayer1": "sets won by Player 1",
            "setWonPlayer2": "sets won by Player 2"
        }
