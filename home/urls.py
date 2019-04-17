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
    path('home/profile/<str:username>/changepassword/', views.changepassword, name='changepassword'),
    #LIST OF FOLLOWERS PAGE
    path('home/profile/<str:username>/followers/', views.followers_page, name='followers'),
    #CHANGE OF PROFILE
    path('home/profile/<str:username>/change/', views.profilechange, name='profilechange'),
    #DELETE POST
    path('home/post/<int:pk>/delete/', views.deletepost, name='delete_post'),
    #LIKE POST
    path('home/post/<int:pk>/like/', views.like_post, name='like_post'),
    #UNLIKE POST
    path('home/post/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
    #FOLLOW
    path('home/profile/<str:username>/add/', views.follow, name='add_friend'),
    #UNFOLLOW
    path('home/profile/<str:username>/delete/', views.unfollow, name='unfollow'),
    #CHANGE PROFILE PICTURE
    path('home/profile/<str:username>/change_profilepicture', views.changeprofilepicture, name='profilepicturechange'),
    #UPLOAD PICTURE
    path('home/profile/<str:username>/upload_picture/', views.picture_upload, name='profilepictureupload'),




]
