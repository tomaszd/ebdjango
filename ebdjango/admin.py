from django.contrib import admin

# Register your models here.
from ebdjango.models import MatchResult
from ebdjango.models import Player
from ebdjango.models import TVSetting

admin.site.register(TVSetting)
admin.site.register(Player)
admin.site.register(MatchResult)
