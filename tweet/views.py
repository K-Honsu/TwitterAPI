from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView
from .models import *
from .serializer import *


class CreateTweet(ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def create(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tweet created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'failure', 'message': 'Tweet creation failed'}, status=status.HTTP_400_BAD_REQUEST)


class GetandDeleteTweet(RetrieveDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def delete(self, request, pk):
        tweet = get_object_or_404(Tweet, pk=pk)
        tweet.delete()
        return Response({'status': 'success', 'message': 'Tweet deleted successfully'}, status=status.HTTP_200_OK)


class Retweet(APIView):
    serializer_class = RetweetSerializer

    def post(self, request, tweet_id):
        tweet = get_object_or_404(Tweet, pk=tweet_id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            retweet = serializer.save(retweet_id=tweet)
            tweet_serializer = TweetSerializer(tweet)
            response_data = {
                'message': 'Retweet created successfully',
                'tweet': tweet_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikedTweet(APIView):
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        # get the tweet
        tweet_id = kwargs.get('tweet_id')
        tweet = get_object_or_404(Tweet, id=tweet_id)
        like_choice = request.data.get('like_choices', True)

        # check if the user has already liked the tweet
        existing_like = Likes.objects.filter(tweet=tweet).first()
        if existing_like:
            existing_like.like_choices = like_choice
            existing_like.save()
            serializer = self.serializer_class(existing_like)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # create a new like
        like = Likes(tweet=tweet, like_choices=like_choice)
        like.save()
        serializer = self.serializer_class(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetAllLikedTweets(APIView):

    def get(self, request):
        liked_tweet = Likes.objects.all()
        serializer = LikeSerializer(liked_tweet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
