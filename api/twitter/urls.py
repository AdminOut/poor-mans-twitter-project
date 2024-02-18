from twitter.views import TweetList
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register("tweets", TweetList)

urlpatterns = [
    path("", include(router.urls)),
]
