from django.conf.urls import include, url
from django.contrib import admin

import mainsite.views as mainsite_views

urlpatterns = [
    url(r'^$', mainsite_views.home_page), 
]
