"""chatter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include(('home.urls', 'home'), namespace='home')),
    url('message/', include(('message.urls', 'message'), namespace='message')),
    # RESET PASSWORD
    url(r'^reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # RESET PASSWORD DONE
    url(r'^reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # RESET CONFIRM
    url(r'^reset/confirm/(?P<uidb64>[A-Za-z0-9]+)-(?P<token>)', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # RESET COMPLETE
    url(r'reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)