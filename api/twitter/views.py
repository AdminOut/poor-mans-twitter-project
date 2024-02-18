from rest_framework.viewsets import ModelViewSet
from .serializers import TweetSerializer
from .models import Tweet


class TweetList(ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
    """
    List all Tweets, or create a new Tweet.
    """
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
