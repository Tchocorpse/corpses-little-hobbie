from . import views
from django.urls import path

app_name = "hw_test"

urlpatterns = [
    path("Test_separate_input", views.separate_input, name="hw_test_input"),
    path("<int:detail_id>/Test_detail", views.separate_detailed, name="hw_test_detail"),
    path(
        "delete_test/<int:delete_id>",
        views.receive_delete_message,
        name="hw_test_delete",
    ),
    path("", views.receive_test_message, name="hw_test"),
]
