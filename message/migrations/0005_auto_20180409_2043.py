# Generated by Django 2.0.3 on 2018-04-09 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20180409_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='reciepent',
            new_name='recipient',
        ),
    ]
