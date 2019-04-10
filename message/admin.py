from django.contrib import admin
from message import models

admin.site.register(models.Message)
admin.site.register(models.Conversations)
