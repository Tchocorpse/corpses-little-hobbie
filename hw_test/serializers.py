from rest_framework import serializers
from .models import HelloTestMessage


class TestMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloTestMessage
        fields = "__all__"
