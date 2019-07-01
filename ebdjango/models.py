from django.db import models


class TVSetting(models.Model):
    color = models.CharField(max_length=200, default='#0096a6', blank=True, null=True)
    color_search = models.CharField(max_length=200, default='#ffaa3f', blank=True, null=True)
    color_default_background = models.CharField(max_length=200, default='#0096a6', blank=True, null=True)
    color_selected_background = models.CharField(max_length=200, default='#ffaa3f', blank=True, null=True)
    color_text = models.CharField(max_length=200, default='#FFFF00FF', blank=True, null=True)
    grid_width = models.CharField(max_length=200, default='2.0', blank=True, null=True)
    grid_height = models.CharField(max_length=200, default='1.5', blank=True, null=True)
    card_width = models.CharField(max_length=200, default='1.0', blank=True, null=True)
    card_height = models.CharField(max_length=200, default='1.0', blank=True, null=True)

    pub_date = models.DateTimeField('date published')
    size = models.IntegerField()
    themeURL = models.URLField()
    jsonPure = models.CharField(max_length=2000, blank=True, null=True)


class Player(models.Model):
    name = models.CharField(max_length=200, default='PlayerName', blank=True, null=True)

    def __unicode__(self):
        return "{}".format(self.name)

    def __str__(self):
        return "{}".format(self.name)


class MatchResult(models.Model):
    player1 = models.ForeignKey(Player, related_name="player1")
    player2 = models.ForeignKey(Player, related_name="player2")
    setWonPlayer1 = models.IntegerField(default=0)
    setWonPlayer2 = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)
    tournament_name = models.CharField(max_length=200, default="No Tournament")
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return "{} vs {}: {}-{}.  {} {} .  WINNER: {}".format(self.player1.name, self.player2.name, self.setWonPlayer1,
                                                              self.setWonPlayer2, self.tournament_name,
                                                              self.pub_date.strftime('%Y-%m-%d-%H:%M'),
                                                              self.get_winner())

    def __str__(self):
        return "{} vs {}: {}-{}.  {} {} .  WINNER: {}".format(self.player1.name, self.player2.name, self.setWonPlayer1,
                                                              self.setWonPlayer2, self.tournament_name,
                                                              self.pub_date.strftime('%Y-%m-%d-%H:%M'),
                                                              self.get_winner())

    def get_simple_date(self):
        return self.pub_date

    def get_winner(self):
        if (self.setWonPlayer1 == self.setWonPlayer2):
            return "DRAW"
        if self.setWonPlayer1 > self.setWonPlayer2:
            return self.player1
        else:
            return self.player2
        return "No winner"
