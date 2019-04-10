from django.urls import path, include
from message import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('/', views.index, name='home'),
    path('<str:username>/', views.message, name='message'),
    path('<str:username>/<int:message_id>)/edit/', views.editmessage, name='editmessage'),
    path('<str:username>/<int:message_id>)/delete/', views.deletemessage, name='deletemessage'),

]