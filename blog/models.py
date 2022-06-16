from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(object):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_date"] #This is used for default ordering by pushed date
