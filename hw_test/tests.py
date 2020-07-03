from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import HelloTestMessage

import datetime


class TrainingTest(TestCase):
    def test_recent_message(self):
        HelloTestMessage.objects.create(
            hello_title="test recent 1",
            hello_body="test body 1",
            publishing_date=timezone.now(),
        )
        HelloTestMessage.objects.create(
            hello_title="test recent 2",
            hello_body="test body 2",
            publishing_date=timezone.now() - datetime.timedelta(days=2),
        )
        recent_test = HelloTestMessage.objects.order_by("-publishing_date")[0]

        response = self.client.get(reverse("hw_test:hw_test_recent"))
        resp_hm = response.context["hello_message"]

        self.assertEqual(resp_hm, recent_test)

    def test_delete_message(self):
        HelloTestMessage.objects.create(
            hello_title="test delete",
            hello_body="test body delete",
            publishing_date=timezone.now(),
        )

        test_message_for_delete = HelloTestMessage.objects.filter(
            hello_title="test delete"
        )[0]

        self.client.post(
            reverse(
                "hw_test:hw_test_delete",
                kwargs={"delete_id": test_message_for_delete.id},
            ),
            pk=test_message_for_delete.id,
        )

        deletion_check = HelloTestMessage.objects.filter(
            hello_title="test delete"
        ).exists()

        self.assertIs(deletion_check, False)
