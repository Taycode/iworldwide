# Generated by Django 2.0.4 on 2018-04-19 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_message_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='new',
            new_name='read',
        ),
    ]
