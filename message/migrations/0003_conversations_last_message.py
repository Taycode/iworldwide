# Generated by Django 2.0.6 on 2019-04-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_conversations_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversations',
            name='last_message',
            field=models.ManyToManyField(related_name='_conversations_last_message_+', to='message.Message'),
        ),
    ]
