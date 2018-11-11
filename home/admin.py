from django.contrib import admin
from home import models

admin.site.register(models.Post)
admin.site.register(models.UserProfile)
admin.site.register(models.Friends)
admin.site.register(models.User_Pictures)