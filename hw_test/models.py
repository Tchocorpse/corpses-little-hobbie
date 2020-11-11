from django.db import models
from django.utils import timezone


class HelloTestMessage(models.Model):
    hello_title = models.CharField(max_length=20)
    hello_body = models.TextField()
    publishing_dt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.hello_title


class ImageFileModel(models.Model):
    image_file = models.ImageField()


class MessageImageMap(models.Model):
    message_id = models.IntegerField()
    image_id = models.IntegerField()
