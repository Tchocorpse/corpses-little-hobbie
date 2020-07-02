# from . import views
from django.urls import path
from hw_test.views import (
    ReceiveTestMessage,
    ReceiveDeleteMessage,
    SeparateDetailed,
    SeparateInput,
    SeparateRecent,
)

app_name = "hw_test"

urlpatterns = [
    path("Test_separate_input", SeparateInput.as_view(), name="hw_test_input"),
    path(
        "<int:detail_id>/Test_detail", SeparateDetailed.as_view(), name="hw_test_detail"
    ),
    path(
        "delete_test/<int:delete_id>",
        ReceiveDeleteMessage.as_view(),
        name="hw_test_delete",
    ),
    path("", ReceiveTestMessage.as_view(), name="hw_test"),
    path("Test_recent", SeparateRecent.as_view(), name="hw_test_recent"),
]
