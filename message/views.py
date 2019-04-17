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

    conversations = models.Conversations.objects.all().order_by('-last_updated')
    MyFunctions.paginating(request, conversations)
    conversations = page_object
    args = {'conversations': conversations}
    return render(request, 'message/index.html', args)


def message(request, username):

    recipient = User.objects.get(username=username)

    if request.method == 'GET':
        form = forms.MessageForm(request.POST or None)
        arg = {'form': form}
        try:
            conversation = models.Conversations.objects.filter(users_involved=recipient).filter(
                users_involved=request.user).first()
            print(conversation)
            conversation = conversation.messages.all().order_by('-time')
            arg['conversation'] = conversation

        except:
            pass

        return render(request, 'message/message.html', arg)

    elif request.method == 'POST':

        form = forms.MessageForm(request.POST or None)
        if form.is_valid():
            new = models.Message.objects.create(user=request.user)
            new.message = form.cleaned_data['message']
            new.save()
            try:
                conversation = models.Conversations.objects.filter(users_involved=recipient).filter(
                    users_involved=request.user).first()
                print(conversation)
                conversation.messages.add(new)
                conversation.last_message = new
                conversation.save()

            except:
                conversation = models.Conversations.objects.create()
                conversation.users_involved.add(recipient, request.user)
                conversation.messages.add(new)
                conversation.save()


        return redirect('/message/%s' %recipient.username)


def deletemessage(request, username, message_id):
    the_message = models.Message.objects.get(pk=message_id)
    user = User.objects.get(username=username)
    the_message.delete()
    return redirect('/message/%s'%user.username)

