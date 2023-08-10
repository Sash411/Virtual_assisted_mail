from django.urls import re_path,path
from . import views
app_name = 'client'

urlpatterns = [
    re_path(r'^$', views.login, name="login"),
    re_path(r'^options/$', views.options, name="options"),
    re_path(r'^sent/$', views.sent, name="sent"),
    re_path(r'^compose/$', views.compose, name="compose"),
    re_path(r'^inbox/$', views.inbox, name="inbox"),
    re_path(r'^trash/$', views.trash, name="trash"),
    re_path(r'^draft/$', views.draft, name="draft"),
    re_path(r'^register/$', views.register, name = "register")
]
