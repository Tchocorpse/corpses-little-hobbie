from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import HelloTestMessage

import datetime


class TrainingTest(TestCase):
    def test_recent_message(self):
        HelloTestMessage.objects.create(
            hello_title="hello title 1",
            hello_body="test body 1",
            publishing_date=timezone.now(),
        )
        HelloTestMessage.objects.create(
            hello_title="hello title 2",
            hello_body="test body 2",
            publishing_date=timezone.now() - datetime.timedelta(days=2),
        )
        recent_test = HelloTestMessage.objects.order_by("-publishing_date")[0]

        response = self.client.get(reverse("hw_test:hw_test_recent"))
        resp_hm = response.context["hello_message"]

        self.assertEqual(resp_hm, recent_test)
