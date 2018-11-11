from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Message(models.Model):
    users = models.ManyToManyField(User, related_name='+')
    message = models.CharField(max_length=1000)
    recipient = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=True)

    def __str__(self):
        return self.sender + ' sends to ' + self.recipient + ': ' + self.message[:10]

