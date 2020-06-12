from . import views
from django.urls import path

urlpatterns = [
    #path('', views.index, name='hw_test'),
    path('', views.receive_test_message, name='hw_test')
]