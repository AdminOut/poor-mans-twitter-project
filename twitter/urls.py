
from twitter.views import TweetList
from rest_framework import routers
router=routers.DefaultRouter()
router.register('tweetsc', TweetList)

urlpatterns = router.urls
# [
#     path('tweets/', Tweet_list, name='tweet-list'),
# ]
