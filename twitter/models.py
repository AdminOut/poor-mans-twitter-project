from django.db import models

# Create your models here.


class Tweet(models.Model):
    # title
    name = models.CharField(max_length=100)
    message = models.TextField(
        max_length=50, blank=True, null=True)  # description

    # completed
    created_at = models.DateTimeField(auto_now_add=True)  # created_at

    def __str__(self):
        # return the task title
        return self.message
