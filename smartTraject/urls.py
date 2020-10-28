from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.urls import path
from mainApp import views as mainApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainApp.home, name='home'),
    path('baseModify', mainApp.baseModify, name='baseModify'),
    path('rencontres', mainApp.rencontres, name='rencontres'),
    path('clubs', mainApp.clubs, name='clubs'),
    path('rencontre_details', mainApp.rencontre_details, name='rencontre_details'),
    path('club_details', mainApp.club_details,
         name='club_details'),
    path('statistics', mainApp.statistics, name='statistics'),
    path('api', mainApp.ChartData.as_view()),
]


urlpatterns += staticfiles_urlpatterns()
