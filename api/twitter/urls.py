from twitter.views import TweetList
from rest_framework import routers
from django.urls import path, include
from twitter.views import tweet_list

router = routers.DefaultRouter()
router.register("tweets", TweetList)

urlpatterns = [
    path("", include(router.urls)),
    path("tweets_list/", tweet_list, name="tweet-list"),
]
