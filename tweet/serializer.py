from .models import *
from rest_framework import serializers


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'message', 'upload1',
                  'upload2', 'upload3', 'upload4']



class RetweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retweet
        fields = ['id', 'retweet_id']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['id', 'like_choices', 'tweet']
