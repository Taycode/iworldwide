from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + ': ' + self.message[:10]


class Conversations(models.Model):
    users_involved = models.ManyToManyField(User)
    messages = models.ManyToManyField(Message)

