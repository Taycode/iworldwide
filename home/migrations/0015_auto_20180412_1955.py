# Generated by Django 2.0.3 on 2018-04-12 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20180412_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liking',
            name='post',
        ),
        migrations.AddField(
            model_name='liking',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.Post'),
        ),
    ]
