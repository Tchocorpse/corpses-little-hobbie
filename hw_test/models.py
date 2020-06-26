from django.db import models


class HelloTestMessage(models.Model):
    hello_title = models.CharField(max_length=10)
    hello_body = models.TextField()
    publishing_date = models.DateTimeField()

    def __str__(self):
        return self.hello_title
