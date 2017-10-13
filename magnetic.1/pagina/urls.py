 # -*- coding: utf-8 -*-


"""pagina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import *
from django import *
from django.contrib import admin
from centralmovies import views
from centralmovies.models import * 

from django.conf import settings
urlpatterns = [
	
      url(r'^admin/', admin.site.urls),
      url(r'^top250/$', views.rankingIMDB),
      url(r'^top250/ops/$', views.ops),
      url(r'^search/$', views.listaopcao),
      url(r'^games/$', views.games),
      url(r'^games/plataform/(?P<string>[\w\-]+)', views.gamesByGenre),
      url(r'^movies/$', views.movies),
      url(r'^movies/ops/$', views.ops),
      url(r'^series/ops/$', views.ops),
      url(r'^movies/genre/$', views.moviesByGenre),
      url(r'^series/(?P<string>[\w\-]+)', views.seriesByGenre),
      url(r'^title/(?P<id>[\w\-]+)/(?P<season>[\w\-]+)', views.seasonSeries),
      url(r'^movie/id/(?P<id>[\w\-]+)/$', views.moviesByDetail),
      url(r'^tvshow/id/(?P<id>[\w\-]+)/$', views.seriesByDetail),
      url(r'^movies/genre/(?P<string>[\w\-]+)', views.moviesByGenre),
      url(r'^series/topseries/$',views.topSeries),
      url(r'^series/$', views.series),
      url(r'^games/ops/$', views.ops),
      url(r'^ops/$', views.ops),
      url(r'^$', views.home, name='home'),
      

]
