from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.CreateTweet.as_view()),
    path('get_or_delete/<int:pk>/', views.GetandDeleteTweet.as_view()),
    path('tweets/<int:tweet_id>/retweet/', views.Retweet.as_view()),
    path('tweets/<int:tweet_id>/like/', views.LikedTweet.as_view()),
    path('tweets/likes/', views.GetAllLikedTweets.as_view()),
]
