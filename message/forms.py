from django.forms import ModelForm
from django import forms
from message import models

class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ('message',)
