"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets
from django.views.generic import TemplateView

from . import views





urlpatterns = [
                   url('^$', views.index, name='index'),
                   url('^dupa/$', views.index2, name='index2'),
                   url('^example/$', views.example, name='example'),
                   url('^coming_soon/$', views.coming_soon, name='coming_soon'),
                   ####################
                   url('^api/cards/$', views.get_cards, name='get_cards'),
                   url('^api/dynamic/cards/$', views.dynamic_get_cards, name='dynamic_get_cards'),
                   url('^api/resources/$', views.get_resources_files_path, name='get_resources'),
                   url('^api/tvsettings/$', views.tvsettings, name='tvsettings'),
                   url('^api/dynamic/tvsettings/$', views.dynamic_tvsettings, name='dynamic_tvsettings'),
                   url('^api/static/tvsettings/$', views.static_tvsettings, name='static_tvsettings'),
                   # PING PONG!!!!!!!!!
                   url('^players/$', views.players, name='players'),
                   url('^players/(?P<pk>\d+)/matchresults$', views.player_results, name='player_results'),
                   url('^pingpong/results/$', views.pingpong_results, name='pingpong_results'),
                   url('^pingpong/results/static$', views.pingpong_results_static, name='pingpong_results_static'),
                   url('^pingpong/results/new', views.result_new, name='result_new'),
                   # matchresult!!!!!!!!!
                   url('^matchresult/(?P<pk>\d+)$', views.result_edit, name='result_detail'),
                   # snooker
                   url(r'^snooker/$', TemplateView.as_view(template_name='ebdjango/snooker.html'), name="home"),
                   url('^snooker/results/$', views.snooker_results, name='snooker_results'),
                   url('^api/results_list$', views.results_list, name='results_list'),
                   url(r'^admin/', admin.site.urls),

               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
