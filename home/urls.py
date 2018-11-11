from django.conf.urls import url, include
from home import views
from django.contrib.auth.views import login, logout, password_reset_done
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #HOMEPAGE
    url(r'^$', views.index, name='homepage'),
    #MAINPAGE
    url(r'^home/$', views.home, name='home'),
    #LOGIN PAGE
    url(r'^home/login/$', login, {'template_name':'home/login.html'}, name='login'),
    #LOGOUT URL
    url(r'^home/logout/$', logout, {'next_page':'/'}, name='logout'),
    #REGISTRATION PAGE
    url(r'^home/register/$', views.register, name='register'),
    #PROFILE PAGE
    url(r'^home/profile/(?P<username>[A-Za-z0-9]+)/$', views.profilepage, name='profile'),
    #PASSWORD CHANGE
    url(r'^home/profile/(?P<username>[A-Za-z0-9]+)/changepassword/$', views.changepassword, name='changepassword'),
    #LIST OF FOLLOWERS PAGE
    url(r'^home/profile/(?P<username>[A-Za-z0-9]+)/followers/$', views.followerspage, name='followers'),
    #CHANGE OF PROFILE
    url(r'^home/profile/(?P<username>[A-Za-z0-9]+)/change/$', views.profilechange, name='profilechange'),
    #DELETE POST
    url(r'^home/post/(?P<pk>[0-9]+)/delete/$', views.deletepost, name='deletepost'),
    #EDIT POST
    url(r'^home/post/(?P<pk>[0-9]+)/edit/$', views.editpost, name='editpost'),
    #LIKE POST
    url(r'^home/post/(?P<pk>[0-9]+)/like/$', views.likepost, name='likepost'),
    #UNLIKE POST
    url(r'^home/post/(?P<pk>[0-9]+)/unlike/$', views.unlikepost, name='unlikepost'),
    #FOLLOW
    url(r'^home/profile/(?P<username>[A-Za-z0-9]+)/add/$', views.addfriend, name='addfriend'),
    #UNFOLLOW
    url(r'^home/profile/(?P<username>[A-Za-z0-9]+)/delete/$', views.deletefriend, name='unfriend'),
    #CHANGE PROFILE PICTURE
    url(r'^home/profile/(?P<username>[A-Za-z0-9]+)/change_profilepicture', views.changeprofilepicture, name='profilepicturechange'),
    #UPLOAD PICTURE
    url(r'^home/profile/(?P<username>[A-Za-z0-9]+)/upload_picture/$', views.picture_upload, name='profilepictureupload'),




]
