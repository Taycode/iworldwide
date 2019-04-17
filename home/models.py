from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.IntegerField(default=0)
    user_like = models.ManyToManyField(User, related_name='+')

    def __str__(self):
        length = len(self.text)
        if length >= 10:
            return self.user.username + ' - ' + self.text[:10] + '...'
        else:
            return self.user.username + ' - ' + self.text[:10] + '...'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    image = models.FileField(upload_to='profile_image', default='profile_image/codes.png')
    followers = models.ManyToManyField(User, related_name='+')
    following = models.ManyToManyField(User, related_name='+')
    def __str__(self):
        return self.user.username

    def count_followers(self):
        return self.followers.count()

    def count_following(self):
        return self.following.count()

    def list_of_followers(self):
        return self.followers.all()

    def list_of_following(self):
        return self.following.all()


def createprofile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(createprofile, sender=User)




class User_Pictures(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='user_images')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username + ' - ' + self.image.url




class Picture_Post(models.Model):
    image = models.ImageField(upload_to='user_images')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
