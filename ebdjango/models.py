from django.db import models


class TVSetting(models.Model):
    color = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    size = models.IntegerField()
    cos= models.URLField()


