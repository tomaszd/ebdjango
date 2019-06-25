from django.db import models


class TVSetting(models.Model):
    color = models.CharField(max_length=200, default='#0096a6', blank=True, null=True)
    color_search = models.CharField(max_length=200, default='#ffaa3f', blank=True, null=True)
    color_default_background = models.CharField(max_length=200, default='#0096a6', blank=True, null=True)
    color_selected_background = models.CharField(max_length=200, default='#ffaa3f', blank=True, null=True)
    color_text = models.CharField(max_length=200, default='#FFFF00FF', blank=True, null=True)
    grid_width = models.CharField(max_length=200, default='2.0', blank=True, null=True)
    grid_height = models.CharField(max_length=200, default='1.5', blank=True, null=True)

    pub_date = models.DateTimeField('date published')
    size = models.IntegerField()
    themeURL = models.URLField()
    jsonPure = models.CharField(max_length=2000, blank=True, null=True)
