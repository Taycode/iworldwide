from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from message import models, forms
from home import models as home_models
from django.urls import reverse
from datetime import timezone
from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
page_object = []
class MyFunctions:
    def paginating(request, object):
        global page_object
        paginator = Paginator(object, 20)

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
            return page_object


def index(request):

    users = User.objects.all().order_by('-last_login')
    MyFunctions.paginating(request, users)

    users = page_object
    myuser = request.user
    args = {'users':users,'myuser':myuser}
    return render(request, 'message/index.html', args)


def message(request, username):

    recipient = User.objects.get(username = username)
    recipient_profile = home_models.UserProfile.objects.get(user=recipient)
    if request.method == 'GET':
        themessages = []
        form = forms.MessageForm()
        myuser = request.user
        messages = models.Message.objects.all().order_by('-time')
        for message in messages:
            if myuser in message.users.all() and recipient in message.users.all():
                themessages.append(message)
        count = 0
        for chatmessage in themessages:
            if chatmessage.read == True and chatmessage.sender == recipient.username:
                count += 1
                chatmessage.read = False
                chatmessage.save()
        print(count)
        MyFunctions.paginating(request, themessages)
        messages = page_object

        args = {'messages': messages, 'form':form, 'recipient':recipient, 'myuser':myuser, 'profile':recipient_profile}
        return render(request, 'message/message.html', args)

    elif request.method == 'POST':

        form = forms.MessageForm(request.POST or None)
        if form.is_valid():
            new = models.Message.objects.create()
            new.message = form.cleaned_data['message']
            new.sender = request.user.username
            new.recipient = recipient.username
            new.users.add(request.user)
            new.users.add(recipient)
            new.save()



        return redirect('/message/%s' %recipient.username)


def editmessage(request, username, message_id):
    the_message = models.Message.objects.get(pk=message_id)
    user = User.objects.get(username=username)
    form = forms.MessageForm(request.POST or None, instance=the_message)
    if request.method == 'GET':
        args = {'form':form}
        return render(request, 'message/editmessage.html', args)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/message/%s'%user.id)

def deletemessage(request, username, message_id):
    the_message = models.Message.objects.get(pk=message_id)
    user = User.objects.get(username=username)
    the_message.delete()
    return redirect('/message/%s'%user.username)

