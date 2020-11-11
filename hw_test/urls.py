from django.urls import path
from hw_test.views import (
    ReceiveMessage,
    ReceiveDeleteMessage,
    SeparateDetailed,
    SeparateInput,
    SeparateRecent,
    LegacyReceiveMessage,
    LegacyDeleteMessage,
    LegacyInput,
    SeparateImageOutput,
)

app_name = "hw_test"

urlpatterns = [
    path("Test_separate_input", LegacyInput.as_view(), name="hw_test_input"),
    path(
        "<int:detail_id>/Test_detail", SeparateDetailed.as_view(), name="hw_test_detail"
    ),
    path(
        "delete_test/<int:delete_id>",
        LegacyDeleteMessage.as_view(),
        name="hw_test_delete",
    ),
    path("", LegacyReceiveMessage.as_view(), name="hw_test"),
    path("Test_recent", SeparateRecent.as_view(), name="hw_test_recent"),
    path("sendmes", SeparateInput.as_view(), name="send_message"),
    path("deletemes", ReceiveDeleteMessage.as_view(), name="delete_message"),
    path("receivemes", ReceiveMessage.as_view(), name="receive_message"),
    path("image/<int:message_id>", SeparateImageOutput.as_view(), name="image_output")
]

