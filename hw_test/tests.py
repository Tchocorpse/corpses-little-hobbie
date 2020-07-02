from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import HelloTestMessage

import datetime


class TrainingTest(TestCase):
    def test_recent_message(self):
        recent_test = HelloTestMessage.objects.order_by("-publishing_date")[0]

        HelloTestMessage.objects.create(
            hello_title="test_recent",
            hello_body="test_body",
            publishing_date=timezone.now(),
        )
        response = self.client.get("hw_test/Test_recent.html")

        self.assertQuerysetEqual(response.context["hello_message"], recent_test)
