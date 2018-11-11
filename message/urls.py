from django.conf.urls import url, include
from message import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^(?P<username>[A-Za-z0-9]+)/$', views.message, name='message'),
    url(r'^(?P<username>[A-Za-z0-9]+)/(?P<message_id>[A-Za-z0-9]+)/edit/$', views.editmessage, name='editmessage'),
    url(r'^(?P<username>[A-Za-z0-9]+)/(?P<message_id>[A-Za-z0-9]+)/delete/$', views.deletemessage, name='deletemessage'),

]