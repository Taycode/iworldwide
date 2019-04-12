from django.urls import path
from django.conf.urls import url, include
from home import views
from django.contrib.auth.views import login, logout, password_reset_done
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #HOMEPAGE
    path('', views.index, name='homepage'),
    #MAINPAGE
    path('home/', views.home, name='home'),
    #LOGIN PAGE
    path('home/login/', views.loginView, name='login'),
    #LOGOUT URL
    path('home/logout/', logout, {'next_page': '/'}, name='logout'),
    #REGISTRATION PAGE
    path('home/register/', views.register, name='register'),
    #PROFILE PAGE
    path('home/profile/<str:username>/', views.profilepage, name='profile'),
    #PASSWORD CHANGE
    path('home/profile/<str:username>/changepassword/$', views.changepassword, name='changepassword'),
    #LIST OF FOLLOWERS PAGE
    path('home/profile/<str:username>/followers/', views.followerspage, name='followers'),
    #CHANGE OF PROFILE
    path('home/profile/<str:username>/change/', views.profilechange, name='profilechange'),
    #DELETE POST
    path('home/post/<int:pk>/delete/', views.deletepost, name='deletepost'),
    #EDIT POST
    path('home/post/<int:pk>/edit/', views.editpost, name='editpost'),
    #LIKE POST
    path('home/post/<int:pk>/like/', views.likepost, name='likepost'),
    #UNLIKE POST
    path('home/post/<int:pk>/unlike/', views.unlikepost, name='unlikepost'),
    #FOLLOW
    path('home/profile/<str:username>/add/', views.addfriend, name='addfriend'),
    #UNFOLLOW
    path('home/profile/<str:username>/delete/', views.deletefriend, name='unfriend'),
    #CHANGE PROFILE PICTURE
    path('home/profile/<str:username>/change_profilepicture', views.changeprofilepicture, name='profilepicturechange'),
    #UPLOAD PICTURE
    path('home/profile/<str:username>/upload_picture/', views.picture_upload, name='profilepictureupload'),




]
