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
from django.conf.urls import url
from django.contrib import admin
import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url('^$', views.index, name='index'),
                  url('^dupa/$', views.index2, name='index2'),
                  url('^example/$', views.example, name='example'),
                  url('^coming_soon/$', views.coming_soon, name='coming_soon'),
                  url('^api/cards/$', views.get_cards, name='get_cards'),
                  url('^api/dynamic/cards/$', views.dynamic_get_cards, name='dynamic_get_cards'),
                  url('^api/tvsettings/$', views.tvsettings, name='tvsettings'),
                  url('^api/dynamic/tvsettings/$', views.dynamic_tvsettings, name='dynamic_tvsettings'),
                  url('^api/static/tvsettings/$', views.static_tvsettings, name='static_tvsettings'),
                  url('^pingpong/players/$', views.pingpong_players, name='pingpong_players'),
                  url('^pingpong/results/$', views.pingpong_results, name='pingpong_results'),
                  url('^pingpong/results/static$', views.pingpong_results_static, name='pingpong_results_static'),
                  url(r'^admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
