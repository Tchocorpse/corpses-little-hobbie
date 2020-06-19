from . import views
from django.urls import path

app_name = "hw_test"

urlpatterns = [
    path('delete_test/<int:delete_id>', views.receive_delete_message, name='hw_test_delete'),
    path('', views.receive_test_message, name='hw_test')
]

