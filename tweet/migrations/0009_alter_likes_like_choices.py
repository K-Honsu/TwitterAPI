# Generated by Django 3.2.18 on 2023-04-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0008_rename_likes_likes_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='like_choices',
            field=models.BooleanField(choices=[(True, 'Like'), (False, 'Dislike')]),
        ),
    ]
