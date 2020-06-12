from django.db import models
from django.utils import timezone


class HelloTestMessage(models.Model):
    hello_title = models.CharField(max_length=10)
    hello_body = models.TextField()
    publishing_date = models.DateTimeField()

    def receive_message(self):

        self.publishing_date = timezone.now()
        self.save()

    def __str__(self):
        return self.hello_title
