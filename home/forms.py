from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from home import models
from django.contrib.auth.models import User
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ('text',)


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

class ProfileChangeForm(ModelForm):
    class Meta:
        model = models.UserProfile
        exclude = ('user','image')


class Picture_Upload(ModelForm):
    class Meta:
        model = models.User_Pictures
        fields = ['image',]

class ProfilepicChangeForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['image',]

class PicturePostForm(ModelForm):
    class Meta:
        model = models.Picture_Post
        fields = ['image']