
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.files.storage import FileSystemStorage
from home import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


def index(request):
    return redirect('home:home')


@login_required
def home(request):
    if request.method == 'GET':

        myuser = request.user
        form = PostForm
        posts = models.Post.objects.all().order_by('-time')
        paginator = Paginator(posts, 20)

        # get the page parameter from the query string
        # if page parameter is available get() method will return empty string ''
        page = request.GET.get('page')

        try:
            # create Page object for the given page
            page_object = paginator.page(page)
        except PageNotAnInteger:
            # if page parameter in the query string is not available, return the first page
            page_object = paginator.page(1)
        except EmptyPage:
            # if the value of the page parameter exceeds num_pages then return the last page
            page_object = paginator.page(paginator.num_pages)
        theposts = page_object

        args = {'form':form, 'posts':theposts, 'myuser':myuser}
        return render(request, 'home/home.html', args)
    elif request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
        return redirect('home:home')


def loginView(request):
    from .forms import LoginForm
    form = LoginForm
    if request.method == 'GET':
        return render(request, 'home/login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        login_user = User.objects.filter(email=email)
        if login_user:
            if login_user.count() == 1:
                username = login_user.first().username
                login_user = authenticate(username=username, password=password)
                print(login_user, email, password)
                if login_user is not None:
                    if login_user.is_active:
                        print('user is active')
                        login(request, login_user)
                        return redirect('home:home')
                    else:
                        messages.add_message(request, messages.INFO, 'User is inactive')
                        return redirect('home:login')
                else:
                    messages.add_message(request, messages.WARNING , 'Password seems to be incorrect')
                    return redirect('home:login')
            else:
                messages.add_message(request, messages.WARNING , 'an account with the inputted email does not exist')
                return redirect('home:login')
    return redirect('home:login')


def register(request):
    if request.method == 'GET':
        form = RegisterForm
        args = {'form':form,}
        return render(request, 'home/register.html', args)
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            myform = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            myform.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')
        return render(request, 'home/register.html', {'form':form})


def profilepage(request, username):

    user = User.objects.get(username=username)
    profile = models.UserProfile.objects.get(user=user)
    myboolean = user == request.user
    followers = profile.list_of_followers()
    following = profile.list_of_following()

    #USER POSTS
    form = PostForm
    posts = models.Post.objects.filter(user=user).order_by('-time')
    paginator = Paginator(posts, 5)

    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string ''
    page = request.GET.get('page')

    try:
        # create Page object for the given page
        page_object = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        page_object = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        page_object = paginator.page(paginator.num_pages)
    theposts = page_object

    args = {'user':user, 'profile':profile,
            'myboolean':myboolean,'posts':theposts,
            'following':following, 'followers':followers
            }
    return render(request, 'home/profile.html', args)


def profilechange(request, username):
    user = get_object_or_404(User, username=username)
    instance = get_object_or_404(models.UserProfile, user=user)
    form = ProfileChangeForm(request.POST or None,instance=instance)
    if request.method == 'GET':
        args = {'form':form}
        return render(request, 'home/profilechange.html', args)
    elif request.method == 'POST':

        if form.is_valid:
            saved = form.save(commit=False)
            saved.user = request.user
            if 'image' in request.POST:
                if saved.image:
                    saved.image = request.POST.get('image')
                else:
                    saved.image = 'profile_image/whatsapponpc.png'
            saved.save()
            return redirect('home:profile', username=request.user.username)



def deletepost(request, pk):
    post = models.Post.objects.get(pk=pk)
    post.delete()
    return redirect('home:home')


def editpost(request, pk):
    post = models.Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'GET':
        args = {'form':form}
        return render(request, 'home/editpost.html', args)
    elif request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('home:home')


def follow(request, username):
    user = User.objects.get(username=username)
    my_profile = models.UserProfile.objects.get(user=request.user)
    profile = models.UserProfile.objects.get(user=user)
    my_profile.following.add(user)
    profile.followers.add(request.user)
    return redirect('home:profile', username=username)

def unfollow(request, username):
    user = User.objects.get(username=username)
    my_profile = models.UserProfile.objects.get(user=request.user)
    profile = models.UserProfile.objects.get(user=user)
    my_profile.following.remove(user)
    profile.followers.remove(request.user)
    return redirect('home:profile', username=username)


def like_post(request, pk):
    user = request.user
    post = models.Post.objects.get(pk=pk)
    post.number_of_likes += 1
    post.user_like.add(user)
    post.save()
    return redirect('home:home')


def unlike_post(request, pk):
    post = models.Post.objects.get(pk=pk)
    user = request.user
    post.user_like.remove(user)
    post.number_of_likes -= 1
    post.save()
    return redirect('home:home')


def followers_page(request, username):
    user = User.objects.get(username=username)
    profile = models.UserProfile.objects.get(user=user)
    list_of_followers = profile.list_of_followers()
    args = {'followers': list_of_followers, 'profile': profile, 'user': user}
    return render(request, 'home/followers.html', args)

def changepassword(request, username):
    if request.method == 'GET':
        form =  PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'home/changepassword.html', args)
    elif request.method == 'POST':
        form = PasswordChangeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home:profile', username=request.user.username)


def picture_upload(request, username):
    user = User.objects.get(username=username)
    if request.method == "GET":
        form = Picture_Upload
        args = {'form': form}
        return render(request, 'home/addpictures.html', args)
    if request.method == 'POST':
        form = Picture_Upload(request.POST, request.FILES)
        if form.is_valid:
            saved = form.save(commit=False)
            saved.user = request.user
            saved.save()
            return redirect('home:profile', username=request.user.username)


def changeprofilepicture(request, username):
    user = User.objects.get(username=username)

    userprofile = models.UserProfile.objects.get(user=user)

    if request.method == 'GET':
        form = ProfilepicChangeForm(instance=userprofile)
        args = {'form':form}
        return render(request, 'home/addpictures.html', args)

    if request.method == 'POST':
        form = ProfilepicChangeForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid:
            saved = form.save(commit=False)

            saved.save()
            return redirect('home:profile', username=request.user.username)
